require 'rubygems'
require 'google/api_client'
require 'launchy'

client = Google::APIClient.new
drive = client.discovered_api('drive', 'v2')

# Initialize OAuth 2.0 client    
client.authorization.client_id = '525402384233-lg16n5981raug5jc2ou8rghs2je0s16d.apps.googleusercontent.com'
client.authorization.client_secret = 'zaITwVEagm-bYu4sSd-Z3-T4'
client.authorization.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

client.authorization.scope = 'https://www.googleapis.com/auth/plus.me'

# Request authorization
uri = client.authorization.authorization_uri
Launchy.open(uri)
puts "enter auth code"
# Wait for authorization code then exchange for token
client.authorization.code = gets.chomp
client.authorization.fetch_access_token!

file = drive.files.insert.request_scheme.new({
	'title' => 'My document',
	'description' => 'A test document',
	'mimeType' => 'text/plain'
})

media = Google::APIClient::UploadIO.new('document.txt', 'text/plain')

# Make an API call
result = client.execute(
  :api_method => drive.files.insert,
  :body_object => file,
  :media => media,
  :parameters => {
    'uploadType' => 'multipart',
    'alt' => 'json'})


jj result.data.to_hashr
#lakdsjfalh