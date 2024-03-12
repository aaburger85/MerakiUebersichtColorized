// this is the shell command that gets executed every time this widget refreshes
export const command = "$(which python3) ./WifiDataMerakiColorized.widget/MerakiSwitch/WifiLine.Meraki.MS.py";
// the refresh frequency in milliseconds
export const refreshFrequency = 1000;

export const className = `
	color: #fff;
	font-family: sans-serfi, helvetica, arial;
	left: 5;
	top: 50px;
	text-align: justify;
	background-color: rgba(0, 0, 0, 0.6);
	margin-left: 10px;
	margin-top: 8px;
	padding: 5 px;
	
	h1 {
		font-size: .75em;
		font-weight: 100;
		margin: 0;
		padding-left: 5px;
		padding-right: 5px;
	}
`;

export const render = ({ output }) => {
//   console.log(output);
  return <h1>{output}</h1>;
};
