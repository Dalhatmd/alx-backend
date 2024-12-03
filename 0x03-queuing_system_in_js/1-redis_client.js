import redis from 'redis';

const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379,
    db: 0
});

client.on('connect', () => {
    console.log(" Redis client connected to the server");
});

client.on('error', (err) => {
    console.log("Redis client not connected to the server: " + err);
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error('Error setting key:', err);
        } else {
            console.log('Reply: ', reply);
        }
    });
};

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error('error: ', err);
        } else {
            console.log(reply);
        }
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
