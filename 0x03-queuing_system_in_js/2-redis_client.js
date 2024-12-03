import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379,
    db: 0
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () => {
    console.log(" Redis client connected to the server");
});

client.on('error', (err) => {
    console.log("Redis client not connected to the server: " + err);
});

const setNewSchool = async(schoolName, value) => {
    try {
        const reply = await setAsync(schoolName, value);
        console.log("Reply: ", reply);
    } catch(err) {
        console.error("Error setting key: ", err);
    }
};

const displaySchoolValue = async(schoolName) => {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch(err) {
        console.error("Error receiving key: ", err);
    }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
