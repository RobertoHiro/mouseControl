import positionOfImage
import os

# os.startfile("dmmgameplayer://play/GCL/priconner/cl/win")
#position = positionOfImage.clickOnImage("img/000-login_bonus.png")

from discord_webhook import DiscordWebhook

webhookUrl = "https://discord.com/api/webhooks/1069728531220799498/MASmaWVY6gYKjYqiqzBnybvortVOttHO9gEMSijXIfECsImn96iYb1lRYlHa_Czz2SR3"
webhook = DiscordWebhook(url=webhookUrl, content='Webhook Message')
response = webhook.execute()