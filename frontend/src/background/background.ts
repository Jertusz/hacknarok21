import { ALL_EVENTS } from './EventTypes';
import WS_MESSAGE_TYPES from './WSMessageTypes';

let ws: WebSocket;
let eventListeners = new Map();

export const BACKGROUND_TARGET_ID = 'background.js';

for (const item of Object.values(ALL_EVENTS)) {
    eventListeners.set(item, []);
}

function processOnMessageEventListeners(event: MessageEvent) {
    const data = JSON.parse(event.data);
    const listeners = eventListeners.get(data.type);

    console.log('sending', event, data);
    listeners.forEach((c: string) => {
        browser.runtime.sendMessage({ for: 'Communicator.ts', call: c, data });
    });
    window.open("popup.html", "extension_popup", "width=300,height=400,status=no,scrollbars=yes,resizable=no");
}

browser.runtime.onMessage.addListener(function (
    request: { for: string; type: WS_MESSAGE_TYPES; content: any },
    sender,
    sendResponse
) {
    if (request.for === BACKGROUND_TARGET_ID) {
        switch (request.type) {
            case WS_MESSAGE_TYPES.CONNECT: {
                if (ws !== undefined) ws.close();
                ws = new WebSocket(request.content);
                console.log(eventListeners);
                ws.onmessage = processOnMessageEventListeners;
                break;
            }
            case WS_MESSAGE_TYPES.SEND_GENERIC: {
                if (ws && ws.OPEN) {
                    ws.send(JSON.stringify(request.content));
                } else {
                    console.log('ws not connected');
                }
                break;
            }
            case WS_MESSAGE_TYPES.SEND_EVENT: {
                if (ws && ws.OPEN) {
                    ws.send(JSON.stringify({ type: request.content.type, ...request.content.content }));
                } else {
                    console.log('ws not connected');
                }
                break;
            }
            case WS_MESSAGE_TYPES.DISCONNECT: {
                ws.close();
                eventListeners = new Map();
                for (const item of Object.values(ALL_EVENTS)) {
                    eventListeners.set(item, []);
                }
                break;
            }
            case WS_MESSAGE_TYPES.REGISTER: {
                const arr = eventListeners.get(request.content.event);
                arr.push(request.content.id);
                eventListeners.set(request.content.event, arr);
                break;
            }
            case WS_MESSAGE_TYPES.UNREGISTER: {
                let arr = eventListeners.get(request.content.event);
                arr = arr.filter((elem: string) => elem === request.content.id);
                eventListeners.set(request.content.event, arr);
                break;
            }
        }
    }

    // browser.tabs.executeScript({
    //   file: "content-script.js",
    // });
});
