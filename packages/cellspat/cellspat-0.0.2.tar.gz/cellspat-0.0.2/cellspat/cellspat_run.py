from libpysal.weights import DistanceBand
from statsmodels.stats.multitest import multipletests
from shapely.geometry import Point
from geopandas import points_from_xy, GeoDataFrame
from scipy.stats import hypergeom, gaussian_kde
from tqdm import tqdm
from numpy import where, median, transpose, vstack
from pandas import DataFrame, read_csv, concat
from esda.getisord import G_Local

def run_cellspat(sdata, df):
    
    '''
    Takes spatial anndata and a dataframe of cellchat interactions and 
    returns the most significant spatially co-localized interactions for each interaction
    
    sdata: spatial anndata object
    
    df: dataframe
        a dataframe of significant cellchat interactions based on scRNASeq
        
    '''
    out = []
    total_spots = sdata.shape[0]  # Total spots in spatial dataset
    df = df.reset_index(drop=True)

    for a, b in tqdm(zip(df.ligand, df.receptor)):
        a = [x.capitalize() for x in a.split('_')]
        b = [x.capitalize() for x in b.split('_')]

        i_a = where(sdata.var_names.isin(a))[0]
        i_b = where(sdata.var_names.isin(b))[0]

        a_x = sdata.X[:, i_a].toarray() # Extract spatial slice
        b_x = sdata.X[:, i_b].toarray()

        for j in range(a_x.shape[1]):
            median_val = median(a_x[a_x[:,j] != 0]) # Binarize cell positivity based on non-zero median
            a_x[:, j] = where(a_x[:, j] > median_val, 1, 0)



        for j in range(b_x.shape[1]):
            median_val = median(b_x[b_x[:,j] != 0])
            b_x[:, j] = where(b_x[:, j] > median_val, 1, 0)



        a_sum = a_x.sum(axis = 1)
        a_c = a_sum == a_x.shape[1]

        b_sum = b_x.sum(axis = 1)
        b_c = b_sum == b_x.shape[1]

        c = transpose(vstack((a_c, b_c)))

        s = c.sum(axis=1)  # 0: no genes, 1: only 1 gene positive, 2: both positive

        n_spots = (s > 0).sum()  # Spots with at least one gene expressed
        n_both = (s > 1).sum()  # Spots with both genes expressed

        # Number of spots where each gene is expressed
        n_gene_a = (c[:, 0] > 0).sum() 
        n_gene_b = (c[:, 1] > 0).sum() 
        out.append([a, b, n_spots, n_both, n_gene_a, n_gene_b, total_spots])

    resy = DataFrame(out, columns = ['gene_a', 'gene_b', 'n_atleast_1', 'n_both', 'n_gene_a', 'n_gene_b', 'total_spots'])


    resy['gene_a'] = resy['gene_a'].apply(lambda x: '_'.join(x) if isinstance(x, list) else x)
    resy['gene_b'] = resy['gene_b'].apply(lambda x: '_'.join(x) if isinstance(x, list) else x)

    resy['interaction_name'] = resy['gene_a'] + '_' + resy['gene_b']

    resy['p_value'] = resy.apply(lambda row: hypergeom.sf(row['n_both']-1, row['total_spots'],
                                                                      row['n_gene_a'], row['n_gene_b']), axis=1)

    resy['fdr'] = multipletests(resy['p_value'], method='fdr_bh')[1]
    resy = concat([resy,df],axis=1)
    
    return(resy)






def getis_ord(gene1,gene2,adata):
    
    '''
    Takes spatial anndata and ligand and recptor genes and runs Getis ord Gi* statistical test and
    returns an anndata object with the hotspots of ligand-receptor co-localization
    
    adata: spatial anndata object
    
    gene1: string
        The name of the ligand gene
        
    gene2: string
        The name of the receptor gene   
    
    '''
    
    # Extract spatial coordinates
    
    spatial_coords = DataFrame(adata.obsm["spatial"], index=adata.obs_names, columns=["x", "y"])
    
    # Extract expression values
    expression_df = DataFrame(adata[:, [gene1, gene2]].X.todense(), index=adata.obs_names, columns=[gene1, gene2])

    # Compute a coexpression score (choose one metric)
    expression_df["coexpression"] = expression_df[gene1] * expression_df[gene2]  # Product method

    # Merge with spatial coordinates
    merged_df = spatial_coords.merge(expression_df, left_index=True, right_index=True)

    # Convert to GeoDataFrame
    gdf = GeoDataFrame(merged_df, geometry=points_from_xy(merged_df["x"], merged_df["y"]))
    gdf.set_crs(epsg=4326, inplace=True)  # Set CRS if needed

    
    gdf["coexpression"] = gdf["coexpression"].astype("float64")
    
    # Define spatial weights (distance-based)   
    w = DistanceBand.from_dataframe(gdf, threshold=550, binary=True)  # Adjust threshold
    
    # Compute Getis-Ord Gi*
    gi_star = G_Local(gdf["coexpression"], w)
    
    a = [len(val) for key, val in w.neighbors.items()]
    median(a) #keep median around 24
    
    # Add results to GeoDataFrame
    gdf["Gi*_p"] = gi_star.p_sim # Standardized Z-score
    gdf["Gi*_z"] = gi_star.z_sim # Standardized Z-score

    gdf['pval_hr'] = gi_star.p_z_sim 
    
    
    gdf_no_na = gdf.dropna(subset=['pval_hr'])
    gdf_no_na['fdr_bh'] = multipletests(gdf_no_na['pval_hr'], method='fdr_bh')[1]

    gdf['fdr_bh'] = gdf_no_na['fdr_bh']
    
    gdf["hotspot_bh"] = where((gdf["fdr_bh"] < 0.05) & (gdf["Gi*_z"] > 0), True, False)

    
    adata.obs['Gi*_p'] = gdf['Gi*_p']
    adata.obs['Gi*_z'] = gdf['Gi*_z']
    adata.obs['fdr_bh'] = gdf.fdr_bh
    adata.obs['hotspot_bh'] = gdf.hotspot_bh.astype(int)
    adata.obs['coexpression_Gi'] = gdf.coexpression

    
    
    return(adata)
