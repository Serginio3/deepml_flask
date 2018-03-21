#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from autocorrect import spell

app = Flask("deep_ml")

dict_of_correction_words={}

@app.route('/autocorrect/api/v1.0/correction', methods=['POST'])
def correct_a_word():

    if not request.json or not 'word_for_correction' in request.json:
       abort(400)
    if len(request.json['word_for_correction'].split())!=1:
        abort(400)
    word_for_correction = request.json['word_for_correction']
    if word_for_correction in dict_of_correction_words:
        corrected_word = dict_of_correction_words[word_for_correction]
    else:
        corrected_word = spell(word_for_correction)
     
    return jsonify({'corrected_word': corrected_word}), 201
     
@app.route('/autocorrect/api/v1.0/list_of_words_for_correction', methods=['POST'])
def correct_the_words():
    corrected_words=[]
    if not request.json or not 'list_of_words_for_correction' in request.json:
        abort(400)
    if len(request.json['list_of_words_for_correction'].split())<=1:
        abort(400)
    for word in request.json['list_of_words_for_correction'].split():
        if word in dict_of_correction_words:
            corrected_word=dict_of_correction_words[word]
        else:
            corrected_word = spell(word)
        corrected_words.append(corrected_word)
    return jsonify({'corrected_word': " ".join(corrected_words)}), 201
    
@app.route('/autocorrect/api/v1.0/set_a_correction', methods=['PUT'])
def set_a_corr():
    if not request.json:
        abort(400)
    if len(request.json['pair'].split())!=2:
        abort(400)    
    pair=request.json['pair'].split()
    dict_of_correction_words[pair[0]]=pair[1]
    return jsonify({pair[0]: pair[1]}), 201

      
    
if __name__ == '__main__':
    app.run(debug=True)
