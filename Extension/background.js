chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked(tab){
    let msg = {
        txt: "runSearch"
    }
    chrome.tabs.sendMessage(tab.id, msg);
}