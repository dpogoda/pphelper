"""
Data structure is like this
[
  [
    {
      shortName: "teamA"
      ...
    },
    {
      shortName: "teamB"
      ...
    }
  ]
]
"""
class Filter:
  
  def __init__(self, data):
    self.data = data

  """
  Get the filtered data
  """
  def get(self):
    return self.data

  """
  Get the length of the filtered data
  """
  def length(self):
    return len(self.data)

  """
  Get distinct team names in the filtered data
  """
  def getDistinctTeamNames(self):
    teamNamesId = {}
    for i in range(len(self.data)):
      teamA     = self.data[i][0]['shortName']
      teamB     = self.data[i][1]['shortName']
      if teamA not in teamNamesId:
        teamNamesId[teamA] = teamA
      if teamB not in teamNamesId:
        teamNamesId[teamB] = teamB
    return teamNamesId

  """
  Get all matches were the home team name equals 'name'
  """
  def homeTeamNameEq(self, teamName):
    filtered = []
    for i in range(len(self.data)):
      if self.data[i][0]['shortName'].lower() == teamName.lower():
        filtered.append(self.data[i])
    self.data = filtered
    return self

  """
  Get all matches were the guest team name equals 'name'
  """
  def guestTeamNameEq(self, teamName):
    filtered = []
    for i in range(len(self.data)):
      if self.data[i][1]['shortName'].lower() == teamName.lower():
        filtered.append(self.data[i])
    self.data = filtered
    return self


  """
  Get the id of a player by his last name. If multiple players exist with the name, return multiple values
  """
  def getOptaIdByPlayerLastName(self, playerName):
    playerIds = {}
    for i in range(len(self.data)):
      playersA     = self.data[i][0]['players']
      playersB     = self.data[i][1]['players']

      for p in playersA:
        if p['optaLastName'].lower() == playerName.lower() and p['optaId'] not in playerIds:
          playerIds[p['optaId'] + " " + self.data[i][0]['shortName']] = f"{p['optaFirstName']} {p['optaLastName']}"

      for p in playersB:
        if p['optaLastName'].lower() == playerName.lower() and p['optaId'] not in playerIds:
          playerIds[p['optaId'] + " " + self.data[i][1]['shortName']] = f"{p['optaFirstName']} {p['optaLastName']} {self.data[i][1]['shortName']}"

    return playerIds

  def playerIdEq(self, id):
    filtered = []
    for i in range(len(self.data)):
      playersA     = self.data[i][0]['players']
      playersB     = self.data[i][1]['players']

      for p in playersA:
        if p['optaId'] == id:
          filtered.append(p)

      for p in playersB:
        if p['optaId'] == id:
          filtered.append(p)
    self.data = filtered
    return self
  
  def teamWherePlayerId(self, id):
    filtered = []
    for i in range(len(self.data)):
      playersA     = self.data[i][0]['players']
      playersB     = self.data[i][1]['players']

      for p in playersA:
        if p['optaId'] == id:
          filtered.append(self.data[i][0])

      for p in playersB:
        if p['optaId'] == id:
          filtered.append(self.data[i][1])
    self.data = filtered
    return self

  def getTeamWhereTeamName(self, teamName):
    filtered = []
    for i in range(len(self.data)):
      teamA     = self.data[i][0]
      teamB     = self.data[i][1]
      if teamA['shortName'] == teamName:
        filtered.append(teamA)
      if teamB['shortName'] == teamName:
        filtered.append(teamB)
    self.data = filtered
    return self

  """
  Get distinct players in the filtered data
  """
  def getDistinctPlayerIds(self):
    players = {}
    for i in range(len(self.data)):
      teamA     = self.data[i][0]
      teamB     = self.data[i][1]
      playersA  = teamA['players']
      playersB  = teamB['players']

      for p in playersA:
        if p['optaId'] not in players:
          players[p['optaId']] = p

      for p in playersB:
        if p['optaId'] not in players:
          players[p['optaId']] = p

    return players

  """
  Number of wins / number of total matches (of any team)
  """
  def victoryGivenPlayer(self, playerKickerId):
    numberOfWins    = 0.
    numberOfMatches = 0.
    for i in range(len(self.data)):
      teamA        = self.data[i][0]
      teamB        = self.data[i][0]
      playersA     = teamA['players']
      playersB     = teamB['players']

      for p in playersA:
        if p['optaId'] == playerKickerId:
          numberOfMatches += 1
          if teamA['win'] == True:
            numberOfWins += 1

      for p in playersB:
        if p['optaId'] == playerKickerId:
          numberOfMatches += 1
          if teamA['win'] == True:
            numberOfWins += 1

    if numberOfMatches == 0:
      return 0
    return numberOfWins / numberOfMatches