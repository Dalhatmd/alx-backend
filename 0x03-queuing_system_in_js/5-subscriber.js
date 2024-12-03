import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
    console.log("Redis client connected to the server");
})
.on ('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

subscriber.subscribe('holberton school channel', (err) => {
    if (err) {
        console.log("Failed to subscribe: ", err);
    }
});

subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe(channel, (err) => {
            if (err) {
                console.log("failed to unsubscribe: ", err);
            }
            subscriber.quit();
        });
    } else {
        console.log(message);
    };
});
