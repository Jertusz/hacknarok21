import { ALL_EVENTS } from './EventTypes';
import WS_MESSAGE_TYPES from './WSMessageTypes';

let ws: WebSocket;
const eventListeners = new Map();
for (const item in ALL_EVENTS) {
    eventListeners.set(item, []);
}
console.log(eventListeners);

browser.runtime.onMessage.addListener(function (
    request: { type: WS_MESSAGE_TYPES; content: any },
    sender,
    sendResponse
) {
    switch (request.type) {
        case WS_MESSAGE_TYPES.CONNECT: {
            if (ws !== undefined) ws.close();
            ws = new WebSocket(request.content);
            break;
        }
        case WS_MESSAGE_TYPES.SEND_GENERIC: {
            ws.send(JSON.stringify(request.content));
            break;
        }
        case WS_MESSAGE_TYPES.SEND_EVENT: {
            ws.send(JSON.stringify(request.content));
            break;
        }
        case WS_MESSAGE_TYPES.DISCONNECT: {
            ws.close();
            break;
        }
        case WS_MESSAGE_TYPES.REGISTER: {
            eventListeners.set(request.content.event, request.content.callback);
        }
    }

    // browser.tabs.executeScript({
    //   file: "content-script.js",
    // });
});
