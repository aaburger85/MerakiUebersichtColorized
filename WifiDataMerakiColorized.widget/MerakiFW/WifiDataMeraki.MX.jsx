// this is the shell command that gets executed every time this widget refreshes
export const command = "$(which python3) ./WifiDataMerakiColorized.widget/MerakiFW/WifiLine.Meraki.MX.py";
// the refresh frequency in milliseconds
export const refreshFrequency = 1000;

export const className = `
	color: #fff;
	font-family: sans-serfi, helvetica, arial;
	left: 5;
	top: 70px;
	text-align: justify;
	background-color: rgba(0, 0, 0, 0.6);
	margin-left: 10px;
	margin-top: 12px;
	padding: 5px;
	
	h1 {
		font-size: .75em;
		font-weight: 100;
		margin: 0;
		padding: 0;
	}
`;

export const render = ({ output }) => {
//   console.log(output);
  return <h1>{output}</h1>;
};
