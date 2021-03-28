import { BACKGROUND_TARGET_ID } from './background';
import { ALL_EVENTS } from './EventTypes';
import WS_MESSAGE_TYPES from './WSMessageTypes';

export const COMMUNICATOR_TARGET_ID = 'Communicator.ts';

let eventListeners = new Map();

function callCallbacks(request: any, sender: any, sendResponse: any) {
    if (request.for == COMMUNICATOR_TARGET_ID) {
        const listener = eventListeners.get(request.call);
        listener(request.data);
    }
}
browser.runtime.onMessage.addListener(callCallbacks);

const generateCode = () => {
    const availableCharacters = 'ABCDEFGHIJKLMNOPQRSTVUWXYZabcdefghijklmnopqrstuvxyz123456789';
    let result = '';
    function getRandomInt(min: number, max: number) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    }
    for (let i = 0; i < 12; i++) {
        result += availableCharacters[getRandomInt(0, availableCharacters.length)];
    }
    return result;
};

export class Communicator {
    static connect(url: string): Promise<any> {
        return browser.runtime.sendMessage({ for: BACKGROUND_TARGET_ID, type: WS_MESSAGE_TYPES.CONNECT, content: url });
    }
    static disconnect(): Promise<any> {
        eventListeners = new Map();
        return browser.runtime.sendMessage({
            for: BACKGROUND_TARGET_ID,
            type: WS_MESSAGE_TYPES.DISCONNECT,
            content: '',
        });
    }
    static sendGeneric(event: { type: WS_MESSAGE_TYPES; content: any }): Promise<any> {
        return browser.runtime.sendMessage({
            for: BACKGROUND_TARGET_ID,
            type: WS_MESSAGE_TYPES.SEND_GENERIC,
            content: event,
        });
    }
    static sendEvent(event: ALL_EVENTS, content: any) {
        return browser.runtime.sendMessage({
            for: BACKGROUND_TARGET_ID,
            type: WS_MESSAGE_TYPES.SEND_EVENT,
            content: { type: event, content: content },
        });
    }
    static registerListener(event: ALL_EVENTS, callback: () => null): string {
        const code = generateCode();
        eventListeners.set(code, callback);
        browser.runtime.sendMessage({
            for: BACKGROUND_TARGET_ID,
            type: WS_MESSAGE_TYPES.REGISTER,
            content: { event: event, id: code },
        });
        return code;
    }
    static unregisterListener(event: ALL_EVENTS, handle: string) {
        browser.runtime.sendMessage({
            for: BACKGROUND_TARGET_ID,
            type: WS_MESSAGE_TYPES.UNREGISTER,
            content: { event, id: handle },
        });
    }
}
