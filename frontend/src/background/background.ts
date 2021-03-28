import { ALL_EVENTS } from './EventTypes';
import WS_MESSAGE_TYPES from './WSMessageTypes';

let ws: WebSocket;
const eventListeners = new Map();

for (const item of Object.values(ALL_EVENTS)) {
    eventListeners.set(item, []);
}

console.log(eventListeners);

function processOnMessageEventListeners(event: MessageEvent) {
    const data = JSON.parse(event.data);
    const listeners = eventListeners.get(data.type);

    listeners.forEach((c: string) => {
        browser.runtime.sendMessage({ for: 'Communicator.ts', call: c, data });
    });
}

browser.runtime.onMessage.addListener(function (
    request: { type: WS_MESSAGE_TYPES; content: any },
    sender,
    sendResponse
) {
    switch (request.type) {
        case WS_MESSAGE_TYPES.CONNECT: {
            if (ws !== undefined) ws.close();
            ws = new WebSocket(request.content);
            console.log(eventListeners);
            ws.onmessage = processOnMessageEventListeners;
            break;
        }
        case WS_MESSAGE_TYPES.SEND_GENERIC: {
            ws.send(JSON.stringify(request.content));
            break;
        }
        case WS_MESSAGE_TYPES.SEND_EVENT: {
            ws.send(JSON.stringify({ type: request.content.type, ...request.content.content }));
            break;
        }
        case WS_MESSAGE_TYPES.DISCONNECT: {
            ws.close();
            break;
        }
        case WS_MESSAGE_TYPES.REGISTER: {
            const arr = eventListeners.get(request.content.event);
            arr.push(request.content.id);
            eventListeners.set(request.content.event, arr);
        }
        case WS_MESSAGE_TYPES.UNREGISTER: {
            let arr = eventListeners.get(request.content.event);
            arr = arr.filter((elem:string) => elem === request.content.id);
            eventListeners.set(request.content.event, arr);
        }
    }

    // browser.tabs.executeScript({
    //   file: "content-script.js",
    // });
});
