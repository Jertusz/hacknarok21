import WS_MESSAGE_TYPES from './WSMessageTypes';

export default class Communicator {
    static connect(url: string): Promise<any> {
        return browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.CONNECT, content: url });
    }
    static disconnect(): Promise<any> {
        return browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.DISCONNECT, content: '' });
    }
    static send(event: { type: WS_MESSAGE_TYPES; content: string }): Promise<any> {
        return browser.runtime.sendMessage({ type: WS_MESSAGE_TYPES.SEND, content: event });
    }
}
