import { ALL_EVENTS, GENERIC_EVENTS } from '@/background/EventTypes';
import { Communicator } from '../background/Communicator';

console.log('activityDetector!');

const original_visibility = document.visibilityState;
document.onvisibilitychange = (event) => {
    if (document.visibilityState === 'visible') {
        if (original_visibility === 'visible') {
            Communicator.sendEvent(ALL_EVENTS.GENERIC_EVENT, {
                action: GENERIC_EVENTS.TAB_SWITCHED,
                text: 'Powrócił na oryginalna kartę',
            });
        } else {
            Communicator.sendEvent(ALL_EVENTS.GENERIC_EVENT, {
                action: GENERIC_EVENTS.TAB_SWITCHED,
                text: 'Uruchomił kartę z tytułem: ' + document.title,
            });
        }
    } else {
        if (original_visibility === 'visible') {
            Communicator.sendEvent(ALL_EVENTS.GENERIC_EVENT, {
                action: GENERIC_EVENTS.TAB_SWITCHED,
                text: 'Wyszedł z oryginalnej karty',
            });
        } else {
            Communicator.sendEvent(ALL_EVENTS.GENERIC_EVENT, {
                action: GENERIC_EVENTS.TAB_SWITCHED,
                text: 'Wyszedł z karty z tytułem: ' + document.title,
            });
        }
    }
};
