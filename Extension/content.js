function runSearch(){
    let questions = document.getElementsByClassName('freebirdFormviewerComponentsQuestionBaseTitle exportItemTitle freebirdCustomFont');
    var qs = [];
    for (question of questions){
        q = question.textContent;
        qs.push(q);
        NewSearch(q)
    }
}

function mark_tick(data){
    options = document.getElementsByClassName("docssharedWizToggleLabeledLabelText exportLabel freebirdFormviewerComponentsQuestionRadioLabel")
    for (option of options){
        if (option.textContent == data){
            option.textContent = option.textContent + '✅'
        }
    }
}

function NewSearch(q) { 
    let data = fetch('https://<YOUR_API_URL>/?question='+q)
                .then(res => res.json())
                .then(data => mark_tick(data['answer']))

}

chrome.runtime.onMessage.addListener(runSearch);