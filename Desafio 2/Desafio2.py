classe_de_animais1 = {
    "vertebrado": {
                    "ave":{
                        "carnivoro": "aguia",
                        "onivoro": "pomba",
                    },
                   
                  "mamifero":{
                        "onivoro": "homem",
                        "herbivoro": "vaca",
                  },
        }
}
classe_de_animais2 = {                  
   "invertebrado":{
                    "inseto":{
                          "hematofago": "pulga",
                          "herbivoro": "lagarta",
                    },
                    
                    "anelideo":{
                          "hematofago": "sanguessuga",
                          "onivoro": "minhoca",   
                    }    
                   }
}             
                 

dicionario_1 = {**classe_de_animais1 , **classe_de_animais2} #juntando dicionário
dicionario_2 = dicionario_1 ["invertebrado"]["anelideo"]
print(dicionario_2["onivoro"])