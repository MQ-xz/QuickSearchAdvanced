# QuickSearch Advanced

 <b>QuickSearch Advanced </b> is an advanced version of [QuickSearch](https://github.com/MQ-xz/QuickSearch) which auto searches all questions in Google Form and marks correct answers in the Form itself.


## Demo 

![demo](demo.gif)

## Setup & Running

 For <b>QuickSearch Advanced</b>, we first need to setup API to find the correct answers from Google. You can set it on local or run on any server.


### Pre-requisites:

   - python3
   - pip3

### API Setup:

- Clone or download this repo<br/>
``` git clone https://github.com/MQ-xz/QuickSearchAdvanced.git```<br/>
(extract if zipped)
- Switch to API folder
- install [requirements.txt](/API/requirements.txt)<br/>
``` pip install -r requirements.txt```
- Run [app.py](API/app.py) <br/>
``` python app.py ```


### Extension Setup:

- Switch to [/extension](/Extension) directory.
- In [content.js](/Extension/content.js) replace `YOUR_API_URL` with deployed python API URL
- Install the Extension<br/><br/>
<b>Chrome:</b>
  - Open Extensions from Menu or visit ``` chrome://extensions ```
  - Enable <b>Developer Mode</b>
  - Click on <b>Load unpacked Extension.</b>
  - Select the Extension Files.<br/>
  
  <b>Firefox:</b>
   - Open <b>Add-ons & Themes</b> from Menu.
   - Click the <b>Settings ⚙️</b> icon on top right.
   - Activate <b>debug add-ons</b>.
   - Select <b>Load Temporary add-on</b>.

Enjoy 🔥 and Happy Exams ! 😂.


## Disclaimer

Currently, QuickSearch Advanced only supports Questions from [GeekforGeeks](https://www.geeksforgeeks.org) only. Will be updated soon ⚡️.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
