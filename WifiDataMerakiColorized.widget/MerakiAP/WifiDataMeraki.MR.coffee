command: "/usr/local/bin/python3 ./WifiDataMerakiColorized.widget/MerakiAP/WifiLine.Meraki.MR.py"

refreshFrequency: 1000


render: (output) -> """
  <h1>#{output}</h1>
"""

style: """
  color: #fff
  font-family: Optima
  left: 5
  top: 30px
  text-align: justify

  h1
    font-size: 1em
    font-weight: 100
    margin: 0
    padding: 0
  """
#update: (output)