command: "/usr/local/bin/python3 ./WifiDataMerakiColorized.widget/MerakiSwitch/WifiLine.Meraki.MS.py"

refreshFrequency: 1000


render: (output) -> """
  <h1>#{output}</h1>
"""

style: """
  color: #fff
  font-family: Optima
  left: 5
  top: 50px
  text-align: justify
  background-color: rgba(0, 0, 0, 0.6)
  margin-left: 10px
  padding: 5px

  h1
    font-size: 1em
    font-weight: 100
    margin: 0
    padding: 0
  """
#update: (output)