import WS_MESSAGE_TYPES from './WSMessageTypes';

let ws: WebSocket;

browser.runtime.onMessage.addListener(function (request: { type: WS_MESSAGE_TYPES; content: string }, sender, sendResponse) {
    switch (request.type) {
        case WS_MESSAGE_TYPES.CONNECT: {
            if (ws !== undefined) ws.close();
            ws = new WebSocket(request.content);
            break;
        }
        case WS_MESSAGE_TYPES.SEND: {
            ws.send(request.content);
            break;
        }
        case WS_MESSAGE_TYPES.DISCONNECT: {
            ws.close();
            break;
        }
    }

    // browser.tabs.executeScript({
    //   file: "content-script.js",
    // });
});
