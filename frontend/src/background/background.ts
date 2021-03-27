import MESSAGES from './Messages';

let ws: WebSocket;

browser.runtime.onMessage.addListener(function (request: { type: MESSAGES; content: string }, sender, sendResponse) {
    switch (request.type) {
        case MESSAGES.CONNECT: {
            if (ws !== undefined) ws.close();
            ws = new WebSocket(request.content);
        }
        case MESSAGES.SEND {
            ws.send(request.content)
        }
    }

    // browser.tabs.executeScript({
    //   file: "content-script.js",
    // });
});
