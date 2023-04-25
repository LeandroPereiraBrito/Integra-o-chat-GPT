import openai
from deep_translator import GoogleTranslator 
from flask import Flask, make_response, jsonify,request

#====================================================================
# Inseri a chave do open https://platform.openai.com/account/api-keys 
#====================================================================
openai.api_key = '' # Logando na aplicação 

#=================================
# Função de conexão com API
#=================================
def openai_response(text):
    response = openai.Completion.create(
            model='text-davinci-003',
            prompt=text,
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )
    return traduzir(response['choices'][0]['text']) 

#=================================
# Traduz o texo para inglês 
#=================================
def enviar(pergunta):
    ask = GoogleTranslator(source='auto', target='en').translate(text=pergunta)
    print(openai_response(ask))
#=================================
# Traduz o texo para portugues 
#=================================   
def traduzir(texto):
    return GoogleTranslator(source='auto', target='pt').translate(text=texto)
    
app =Flask(__name__)
#=================================
# Rota da API 
#================================= 
@app.route('/mensagem',methods=['POST'])
def mensagem():
    texto = request.json
    return openai_response(texto["texto"])
    
#=================================
# Starta o serviço
#=================================   
app.run()
	