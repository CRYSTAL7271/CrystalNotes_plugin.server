import requests
from colorama import Fore
from tqdm import tqdm
class Terminal:
	def __init__(self, started):
		if started == False:
			print("Welcome to CrystalNotes: plugin_installer, write help if you need help.")
		usr=input("> ")
		if usr == "help":
			print(">help:\ninstall: install a plugin,\ninfo: see info,\ninfo.online")
			Terminal(True)
			
		if usr == "info":
			f=open("help.txt")
			print(f.read())
			f.close()
			Terminal(True)
		if usr == "install":
			try:
				usr=input("set_plugin_name >> ")
				url = "https://csnotes-plugins.netlify.app/" + usr + ".py"
				ext = ".nc"
				print("Getting url...")
				response = requests.get(url)
				print("Getting text...")
				responset = response.text
				if responset == """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>Page Not Found</title>
    <link href='https://fonts.googleapis.com/css?family=Roboto:400,700&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
    <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
      background: rgb(52, 56, 60);
      color: white;
      overflow: hidden;
      margin: 0;
      padding: 0;
    }

    h1 {
      margin: 0;
      font-size: 22px;
      line-height: 24px;
    }

    .main {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      width: 100vw;
    }

    .card {
      position: relative;
      display: flex;
      flex-direction: column;
      width: 75%;
      max-width: 364px;
      padding: 24px;
      background: white;
      color: rgb(14, 30, 37);
      border-radius: 8px;
      box-shadow: 0 2px 4px 0 rgba(14, 30, 37, .16);
    }

    a {
      margin: 0;
      font-weight: 600;
      line-height: 24px;
      color: #054861;
    }

    a svg {
      position: relative;
      top: 2px;
    }

    a:hover,
    a:focus {
      text-decoration: none;
    }

    a:hover svg path{
      fill: #007067;
    }

    p:last-of-type {
      margin-bottom: 0;
    }

    </style>
  </head>
  <body>
    <div class="main">
      <div class="card">
        <div class="header">
          <h1>Page Not Found</h1>
        </div>
        <div class="body">
          <p>Looks like you've followed a broken link or entered a URL that doesn't exist on this site.</p>
          <p>
            <a id="back-link" href="/">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path fill="#007067" d="M11.9998836,4.09370803 L8.55809517,7.43294953 C8.23531459,7.74611298 8.23531459,8.25388736 8.55809517,8.56693769 L12,11.9062921 L9.84187871,14 L4.24208544,8.56693751 C3.91930485,8.25388719 3.91930485,7.74611281 4.24208544,7.43294936 L9.84199531,2 L11.9998836,4.09370803 Z"/>
              </svg>
              Back to our site
             </a>
          </p>
          <hr><p>If this is your site, and you weren't expecting a 404 for this path, please visit Netlify's <a href="https://answers.netlify.com/t/support-guide-i-ve-deployed-my-site-but-i-still-see-page-not-found/125?utm_source=404page&utm_campaign=community_tracking">"page not found" support guide</a> for troubleshooting tips.
          </p>
        </div>
      </div>
    </div>
    <script>
      (function() {
        if (document.referrer && document.location.host && document.referrer.match(new RegExp("^https?://" + document.location.host))) {
          document.getElementById("back-link").setAttribute("href", document.referrer);
        }
      })();
    </script>
  </body>
</html>
""":
				    print("Not Found.")
				else:
					for char in tqdm(responset):
						pass
					f=open("installed/" + usr + ".py", "w")
					f.write(responset)
					f.close()
					print("Plugin found and installed.")
				Terminal(True)
			except Exception as e:
				print("Failed connecting: no internet or plugin doesnt exists, for more info watch output: " + str(e))
		if usr == "info.online":
			try:
				url = "https://csnotes-plugins.netlify.app/info.txt"
				ext = ".nc"
				print("Getting url ...")
				response = requests.get(url)
				print("Getting text...")
				responset = response.text
				print("\n\n\n_______\n\n" + responset)
				Terminal(True)
			except:
				print("Failed connecting: no internet or server is not online.")
				Terminal(True)
				
		else:
			Terminal(True)

if __name__ == "__main__":
	Terminal(False)
