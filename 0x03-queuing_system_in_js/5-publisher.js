import redis from 'redis';

const publisher= redis.createClient();

publisher.on('connect', () => {
    console.log("Redis client connected to the server");
})
.on ('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const publishMessage = (message, time) => {
    setTimeout(() => {
        publisher.publish('holberton school channel', message, (err) => {
            if (err) {
                console.log("failed to publish: ", err);
            } else {
                console.log(`About to send ${message}`);
            }
        });
    }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
