require 'google/api_client'
client = Google::APIClient.new
plus = client.discovered_api('plus')

# Initialize OAuth 2.0 client    
client.authorization.client_id = '525402384233-lg16n5981raug5jc2ou8rghs2je0s16d.apps.googleusercontent.com'
client.authorization.client_secret = 'zaITwVEagm-bYu4sSd-Z3-T4'
client.authorization.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

client.authorization.scope = 'https://www.googleapis.com/auth/plus.me'

# Request authorization
redirect_uri = client.authorization.authorization_uri

# Wait for authorization code then exchange for token
client.authorization.code = '....'
client.authorization.fetch_access_token!

# Make an API call
result = client.execute(
  :api_method => plus.activities.list,
  :parameters => {'collection' => 'public', 'userId' => 'me'}
)

puts result.data
#lakdsjfalh