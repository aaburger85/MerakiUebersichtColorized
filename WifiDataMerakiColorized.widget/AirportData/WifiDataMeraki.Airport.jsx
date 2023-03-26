// this is the shell command that gets executed every time this widget refreshes
export const command = "$(which python3) ./WifiDataMerakiColorized.widget/AirportData/WifiLine.Airport.py";
// the refresh frequency in milliseconds
export const refreshFrequency = 1000;

export const className =`
	color: #fff;
	font-family: sans-serfi, helvetica, arial;
	text-align: justify;
	background-color: rgba(0, 0, 0, 0.6);
	margin: 0px;
	padding: 0px;
	margin-left: 10px;
	padding-right: 5px;

	div {
		font-size: 0.75em;
		font-weight: 100;
	}
	p {
		margin: 0px;
		padding: 0px;
	}
`;

export const render = ({ output }) => {
	const props = JSON.parse(output)
	if (props.hasOwnProperty("message")) {
		return(<div><p>{props.message}</p></div>)
	}
	const data = Object.entries(props).slice(4)
	const dataStatus = Object.entries(props).slice(0, 5)
	let DataElements = data.map((d, i) => <p style={{paddingLeft: "5px"}} key={i}>{d[0]}:<strong>{d[1]}</strong></p>)
	return( 
  		<div style={{display: "flex"}}>
			<p style={{paddingLeft: "5px"}} >RSSI: <strong style={{color: `${dataStatus[1][1]}`}}>{dataStatus[0][1]}</strong></p>
			<p style={{paddingLeft: "5px"}} >Noise Floor: <strong style={{color: `${dataStatus[3][1]}`}}>{dataStatus[2][1]}</strong></p>
			{DataElements}
  		</div>
	);
};
