curl -i -H "Content-Type: application/json" -X POST -d '{"word_for_correction":"borsedf"}' http://localhost:5000/autocorrect/api/v1.0/correction

{
  "corrected_word": "bored"
}

curl -i -H "Content-Type: application/json" -X PUT -d '{"pair":"borsedf ani"}' http://localhost:5000/autocorrect/api/v1.0/set_a_correction

curl -i -H "Content-Type: application/json" -X POST -d '{"word_for_correction":"borsedf"}' http://localhost:5000/autocorrect/api/v1.0/correction

{
  "corrected_word": "ani"
}

curl -i -H "Content-Type: application/json" -X POST -d '{"list_of_words_for_correction":"applp edfs dfkj qjd"}' http://localhost:5000/autocorrect/api/v1.0/list_of_words_for_correction

{
  "corrected_word": "apply elfs duke QD"
}
