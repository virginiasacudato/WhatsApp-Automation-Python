// node 14v
// npm i

const qrcode = require('qrcode-terminal');
const fs = require("fs")
const {Client} = require('whatsapp-web.js');
var dateFormat = require("dateformat");
const moment = require('moment');

const today = new Date();
let hoy = new Date();
hoy = dateFormat(hoy, "yyyy-mm-dd");
console.log(hoy);
const SESSION_FILE_PATH = './session.json';
data_simi_vencido = []
// Load the session data if it has been previously saved
let sessionData;
if(fs.existsSync(SESSION_FILE_PATH)) {
    sessionData = require(SESSION_FILE_PATH);
}
fs.readFileSync('../listas_simi/lista_simi_'+hoy+'.txt',{encoding: 'utf8', flag: 'r'})
.replace("\r", "").split("\n").map(value => {
    const date_simi = new Date(value.split(" ")[1] + "23:59:59");
    let diferencia = moment(date_simi).add(15,"days").diff(moment(), "days");
    console.log(diferencia);
    if(date_simi){
    
        if((date_simi - today) >= 0){
            data_simi_vencido.push(value)
        }
    }
})



console.log(data_simi_vencido);

// Use the saved values
const client = new Client({
    session: sessionData
});


client.initialize();
client.on("qr", qr => {
    qrcode.generate(qr, {small: true} );
})


const chats_enviar_message = [
    // Telephone numnbers
]
client.on("ready", () => {
    console.log("Listo")

    chats_enviar_message.map(value => {
        const chatId = value +"@c.us"
        message = "Las SIMI's próximas a vencer:\n"+data_simi_vencido.join(", ")
        client.sendMessage(chatId,message);
})

    
})
client.on('authenticated', (session) => {
    sessionData = session;
    fs.writeFile(SESSION_FILE_PATH, JSON.stringify(session), function (err) {
        if (err) {
            console.error(err);
        }
    });
});

client.on("auth_failure" , msg => {
    console.log("Ocurrió un error, mensaje:", msg)
})
