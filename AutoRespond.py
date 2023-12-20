const { Client } = require('discord.js-selfbot-v13');
const client = new Client({
    checkUpdate: false,
});

client.on('ready', async () => {
  console.log(`Ready`);
});

client.on('messageCreate', async (message) => {
  if (message.author.id === client.user.id) return;

  if (message.channelId === 'UrChannelId') {
    message.channel.send('Welcome')
      .catch(console.error);
  }
});

client.login('UrToken');
