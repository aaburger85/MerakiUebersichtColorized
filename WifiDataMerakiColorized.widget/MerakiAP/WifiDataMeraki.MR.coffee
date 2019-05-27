command: "/usr/local/bin/python3 ./WifiDataMerakiColorized.widget/MerakiAP/WifiLine.Meraki.MR.py"

refreshFrequency: 1000


render: (output) -> """
  <h1>#{output}</h1>
"""

style: """
  color: #fff
  font-family: sans-serfi, helvetica, arial
  left: 5
  top: 30px
  text-align: justify
  background-color: rgba(0, 0, 0, 0.6)
  margin-left: 10px
  margin-top: 4px
  padding: 5px

  h1
    font-size: .75 em
    font-weight: 100
    margin: 0
    padding: 0
  """
#update: (output)