from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder='../template', static_folder='../static')

@app.route("/classifier/<comment>", methods=["GET","POST"])  # consider to use more elegant URL in your JS
def classify(comment):
    ##### classify with 4 labels #####
    absolutePath = "C:/Users/uchiha/Desktop/PeaQock/Untitled Folder/interface/"
    #absolute path
    with open(absolutePath + "textClassification/src/vectorizerHateOffense.pk", 'rb') as pickle_file:
        tfVec = pickle.load(pickle_file)
    with open(absolutePath + "textClassification/models/NaiBayOHeModel", 'rb') as pickle_file_model:
        model = pickle.load(pickle_file_model)
    tfPred = tfVec.transform([comment])
    output = model.predict(tfPred)
    if output[0] == 1:
        hate = 1
        offense = 0
    elif output[0] == 2:
        offense = 1
        hate = 0
    elif output[0] == 3:
        offense = 1
        hate = 1
    else:
        offense = 0
        hate = 0

    ##########################################

    ##### Classify by separating classes #####
    '''
    with open(absolutePath + "textClassification/src/vectorizerHate.pk", 'rb') as pickle_file:
        tfVec_h = pickle.load(pickle_file)
    with open(absolutePath + "textClassification/src/vectorizerOffense.pk", 'rb') as pickle_file:
        tfVec_o = pickle.load(pickle_file)
    with open(absolutePath + "textClassification/models/NaBayHateModel", 'rb') as pickle_file_model_h:
        model_hate = pickle.load(pickle_file_model_h)
    with open(absolutePath + "textClassification/models/NaBayOffenseModel", 'rb') as pickle_file_model_o:
        model_offense = pickle.load(pickle_file_model_o)
    tfPred_h = tfVec_h.transform([comment])
    tfPred_o = tfVec_o.transform([comment])
    hate = model_hate.predict(tfPred_h)[0]
    offense = model_offense.predict(tfPred_o)[0]
    '''

    #########################################

    return {"comment": comment, "hate": hate, "offense": offense} 

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == "__main__":
    # here is starting of the development HTTP server
    app.run()
