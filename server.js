const express = require('express');
const multer = require('multer');
const { Client, Intents } = require("discord.js-selfbot-v13");
const { joinVoiceChannel, createAudioPlayer, createAudioResource, StreamType } = require("@discordjs/voice");
const { spawn } = require("child_process");
const ffmpegPath = require('ffmpeg-static'); // Thư viện này giúp chạy nhạc trên hosting

const app = express();
const upload = multer({ dest: '/tmp/' });
app.use(express.json());

// Giao diện Web Điều Khiển
app.get('/', (req, res) => {
    res.send(`
    <html>
    <head><title>Bot Control</title></head>
    <body style="background:#23272a; color:white; font-family:sans-serif; text-align:center;">
        <h2>🎵 Discord Music Web Controller</h2>
        <div style="max-width:400px; margin:auto; background:#2c2f33; padding:20px; border-radius:10px;">
            <input type="text" id="tk" placeholder="Dán Token vào đây" style="width:100%; padding:10px; margin:5px 0;">
            <input type="text" id="ch" placeholder="ID Kênh thoại" style="width:100%; padding:10px; margin:5px 0;">
            <input type="file" id="fi" style="width:100%; margin:10px 0;">
            <button onclick="run()" style="width:100%; padding:10px; background:#5865f2; color:white; border:none; cursor:pointer;">KHỞI CHẠY</button>
            <p id="st"></p>
        </div>
        <script>
            async function run() {
                const st = document.getElementById('st'); st.innerText = "Đang chạy...";
                const fd = new FormData();
                fd.append('token', document.getElementById('tk').value);
                fd.append('channelId', document.getElementById('ch').value);
                fd.append('file', document.getElementById('fi').files[0]);
                const res = await fetch('/api/start', { method: 'POST', body: fd });
                const data = await res.json();
                st.innerText = data.message || data.error;
            }
        </script>
    </body>
    </html>
    `);
});

// Logic xử lý xả nhạc (giữ nguyên logic volume/boost của bạn)
app.post('/api/start', upload.single('file'), async (req, res) => {
    const { token, channelId } = req.body;
    try {
        const client = new Client({ checkUpdate: false });
        await client.login(token);
        const channel = await client.channels.fetch(channelId);
        const connection = joinVoiceChannel({
            channelId: channel.id,
            guildId: channel.guild.id,
            adapterCreator: channel.guild.voiceAdapterCreator,
        });
        const player = createAudioPlayer();
        const ffmpeg = spawn(ffmpegPath, ["-i", req.file.path, "-f", "s16le", "-ar", "48000", "-ac", "2", "pipe:1"]);
        const resource = createAudioResource(ffmpeg.stdout, { inputType: StreamType.Raw });
        connection.subscribe(player);
        player.play(resource);
        res.json({ message: "Bot đã vào kênh và đang phát nhạc!" });
    } catch (e) { res.json({ error: e.message }); }
});

app.listen(process.env.PORT || 3000);
