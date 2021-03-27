import { ALL_EVENTS } from './EventTypes';
import WS_MESSAGE_TYPES from './WSMessageTypes';

class Communicator {
    static connect(url: string): Promise<any> {
        return browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.CONNECT, content: url });
    }
    static disconnect(): Promise<any> {
        return browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.DISCONNECT, content: '' });
    }
    static sendGeneric(event: { type: WS_MESSAGE_TYPES; content: any }): Promise<any> {
        return browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.SEND_GENERIC, content: event });
    }
    static sendEvent(event: ALL_EVENTS, content: string) {
        return browser.runtime.sendMessage({
            type: WS_MESSAGE_TYPES.SEND_EVENT,
            content: { event: event, content: content },
        });
    }
    static registerListener(event: ALL_EVENTS, callback: () => null) {
        browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.REGISTER, content: { event: event, callback: callback } });
    }
}
export default Communicator;
