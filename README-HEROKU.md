# Maksym Kornyev - Portfolio

##### Notes to self regarding re-deployment of the application: 

To re-migrate after an update:

* `heroku push master`
* `heroku pg:reset`
* Diagnose ~> `heroku pg:diagnose --app mkornyev`
* `heroku run bash` (do not use `ps:exec` - it does not effect the dyno)
* makemigrations, migrate, and populate
* Confirm that the changes took effect ~> `heroku pg:info`

# mk