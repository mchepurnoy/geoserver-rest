from src.Geoserver import Geoserver
from src.Postgres import Db

geo = Geoserver()
pg = Db('geonode_data', 'postgres', 'Pxfd#f%Ar', '203.159.29.42')
# geo.create_workspace('try')
# geo.create_coveragestore(r'C:\Users\tek\Desktop\geoserver-rest\data\C_EAR\a_Agriculture\agri_final_proj.tif', workspace='try')
# geo.create_featurestore('try_feature', 'try', 'tajikistan', '203.159.29.40', pg_password='Pxfd#f%Ar')
# geo.publish_featurestore('try', 'try_feature', 'country')
# geo.apply_style('country', 'polygon', 'try')

# geo.create_coveragestyle(r'C:\Users\tek\Desktop\geoserver-rest\data\C_EAR\a_Agriculture\agri_final_proj.tif', 'try')
# geo.test2('try', 'try_feature')

# print(pg.get_columns_names('zones'))
print(pg.get_all_values('zones', 'Zone_'))