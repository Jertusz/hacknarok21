export default class Communicator {
    private static instance: Communicator;

    private constructor();

    static getInstance() {
        if (Communicator.instance === undefined) {
            Communicator.instance = new Communicator();
        }
        return Communicator.instance;
    }

    connect(url: string) {
        return undefined;
    }
    disconnect() {
        return undefined;
    }
    send(event: { type: MESSAGES; content: string }) {
        return undefined;
    }
}
