from ml.models import ml
from django.http import JsonResponse
from rest_framework import generics
from .serializers import IndexViewSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import os
import glob
import pickle
import gensim
import re
import time

class GetSavantName(APIView):


    def get(self, request):
        print('sucsess0')
     
        #get savant name
        name_list=[]
        id_list=[]
        nav_url='https://ns-dal-wtapi.netsync.com:251/nav/get-all-customers'
       
        response=requests.get(nav_url)

        data=response.json()
       # names=(data['Response'])
        print('sucsess1')
        

        
            
        
#         # if Response.status_code==200:
#         #     print('yes')   
#         #     savant_file=('ml/data/savant_data.csv' )  
#         #     path_file_remove = ('ml/models/*.sav' )
#         #     os.remove(savant_file)

#         #     #Removed all file ml module (.sav)    
#         #     files_remove = glob.glob(path_file_remove)
#         #     for f in files_remove:
#         #         os.remove(f)
#         #     print('Removed models files')

            
        
#         #     csv_data = {
#         #     'Client ID':id_list,
#         #     'Active customers': name_list,
#         #     }
            
#         #     df = pd.DataFrame(csv_data)
        
#         #     # genrate new savant name  .csv
#         #     df.to_csv('ml/data/savant_data.csv',mode='a', index=False, header=True)
#         #     print('sucsess')    
            
#         #     def tokenize(txt):
#         #         tokens = re.split('\W', txt)
                
#         #         return tokens


#         #     # genrate new module file (.sav) 
#         #     df['customer_tokenized'] = df['Active customers'].apply(lambda x: tokenize(x.lower()))
#         #     dictionary = gensim.corpora.Dictionary(df['customer_tokenized'])
#         #     # Save the dictionaryy object
#         #     file_name = 'ml/models/dictionary.sav'
#         #     pickle.dump(dictionary, open(file_name, 'wb'))
#         #     corpus = [dictionary.doc2bow(text) for text in df['customer_tokenized']]
#         #     tf_idf = gensim.models.TfidfModel(corpus)

#         #     # Save the tfidf object
#         #     file_name = 'ml/models/tfidf.sav'
#         #     pickle.dump(tf_idf, open(file_name, 'wb'))
#         #     similarity_object = gensim.similarities.Similarity("df['customer_tokenized']", tf_idf[corpus],
#         #                                                     num_features=len(dictionary))

#         #     # Save the similarity object
#         #     file_name = 'ml/models/similarity_object.sav'
#         #     pickle.dump(similarity_object, open(file_name, 'wb'))
#         #     print('added new models file')
                                    
#         # else:
#         #     Response ({"Error": "No Data in API"})               
                    
                
                


        return Response(data,status=status.HTTP_200_OK)





class GetCisscoName(generics.GenericAPIView):
    serializer_class = IndexViewSerializer
   # permission_classes =[IsAuthenticated]
    
    
    def post(self, request):
        
       

        if request.method == 'POST':
            input_name =request.data
            values = list(input_name.values())
            match_name =ml.insert_sys1(values[0])
            

        return JsonResponse(match_name,safe=False)       


