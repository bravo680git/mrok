@	
s	applications|app:list|applications:list|app:available|applications:available|apps	Show a list of all (logged in) available cli applications
s	applications:add|app:add	
s	applications:current|app:current	Show the current application
s	applications:info|app:info	Show application details
s	applications:login|app:login|login	
s	applications:logout|app:logout|app:remove|applications:remove|logout	Remove an application from cli local configuration
s	applications:provisioning|app:prov|app:provisioning|prov:apps|prov:applications	Show all provisioning applications
s	applications:scope|app:scope	Switch scope of current application
s	applications:switch|app:switch	Switch applications
s	app:token	Get a new access token from commerce layer api
s	cli:update|upgrade|latest	Update commerce layer cli
s	cli:version|version	Show installed version of commerce layer cli
s	plugins:available	Show all available commerce layer cli plugins
s	plugins:latest	Show latest version of available plugins
s	checkout	Create checkout urls
s	checkout:order	Create checkout urls starting from an existing order
s	imports	List all the created imports or show details of a single import
s	imports:create|imp:create|import	Create a new import
s	imports:delete|imp:delete	Delete an existing import
s	imports:details|imp:details	Show the details of an existing import
s	imports:group|imp:group	List all the imports related to an import group
s	imports:list|imp:list	List all the created imports
s	imports:types|imp:types	Show online documentation for supported resources
s	microstore	Create microstore urls
s	seeder:check	Execute a check on seeder data
s	seeder:clean	Clean previously imported seeder data
s	seeder:seed|seed	Execute commerce layer seeder
s	token:decode|token:info	Decode a commerce layer access token
s	token:generate	Start a wizard to generate a custom access token
s	token:get	Get a new access token
s	token:revoke	Revoke a commerce layer access token
s	resources	List all the available commerce layer api resources
s	resources:all|all|ra|res:all	Fetch all resources
s	resources:args|res:args	Show all the saved command arguments
s	resources:count|count|res:count|rs:count	Count the number of existent resources
s	resources:create|create|rc|res:create|post	Create a new resource
s	resources:delete|delete|rd|res:delete	Delete an existing resource
s	resources:doc|res:doc|doc	Open the default browser and show the online documentation for the resource
s	resources:fetch|fetch|res:fetch|rf	Retrieve a resource or list a set of resources
s	resources:filters|res:filters	Show a list of all available filter predicates
s	resources:get|get|res:get|rg	Retrieve a resource or list a set of resources
s	resources:list|list|rl|res:list	Fetch a collection of resources
s	relationship|resources:rel|res:rel|res:relationship	Fetch a resource relationship
s	resources:retrieve|retrieve|rr|res:retrieve	Fetch a single resource
s	resources:schema|schema|res:schema|rs	Show the current commercelayer openapi schema version used by the plugin
s	resources:update|update|ru|res:update|patch	Update an existing resource
s	orders	Execute an action on an order
s	orders:approve	Send this attribute if you want to approve a placed order
s	orders:approve_and_capture	Send this attribute if you want to approve and capture a placed order
s	orders:archive	Send this attribute if you want to archive the order
s	orders:authorization_amount_cents	The authorization amount, in cents
s	orders:authorize	Send this attribute if you want to authorize the order's payment source
s	orders:billing_address_clone_id	The id of the address that you want to clone to create the order's billing addre
s	orders:billing_address_same_as_shipping	Send this attribute if you want the billing address to be cloned from the order'
s	orders:cancel	Send this attribute if you want to cancel a placed order
s	orders:capture	Send this attribute if you want to capture an authorized order
s	orders:commit_invoice	Send this attribute if you want commit the sales tax invoice to the associated t
s	orders:create_subscriptions	Send this attribute upon/after placing the order if you want to create order sub
s	orders:customer_payment_source_id	The id of the customer payment source (i
s	orders:nullify_payment_source	Send this attribute if you want to nullify the payment source for this order
s	orders:pending	Send this attribute if you want to move a draft or placing order to pending
s	orders:place	Send this attribute if you want to place the order
s	orders:refresh	Send this attribute if you want to manually refresh the order
s	orders:refund	Send this attribute if you want to refund a captured order
s	orders:refund_invoice	Send this attribute if you want refund the sales tax invoice to the associated t
s	orders:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	orders:save_billing_address_to_customer_address_book	Send this attribute if you want the order's billing address to be saved in the c
s	orders:save_payment_source_to_customer_wallet	Send this attribute if you want the order's payment source to be saved in the cu
s	orders:save_shipping_address_to_customer_address_book	Send this attribute if you want the order's shipping address to be saved in the
s	orders:shipping_address_clone_id	The id of the address that you want to clone to create the order's shipping addr
s	orders:shipping_address_same_as_billing	Send this attribute if you want the shipping address to be cloned from the order
s	orders:start_editing	Send this attribute if you want to edit the order after it is placed
s	orders:stop_editing	Send this attribute to stop the editing for the order and return back to placed
s	orders:unarchive	Send this attribute if you want to unarchive the order
s	orders:update_taxes	Send this attribute if you want to force tax calculation for this order (a tax c
s	orders:validate	Send this attribute if you want to trigger the external validation for the order
s	webhooks	List all the registered webhooks or the details of a single webhook
s	webhooks:create|wh:create	Create a new webhook
s	webhooks:destroy|webhooks:delete|wh:delete|wh:destroy	Destroy an existing webhook
s	webhooks:details|wh:details	Show the details of an existing webhook
s	webhooks:event|wh:event	Show the details of a firedf webhook event
s	webhooks:events|wh:events	List all the events associated to the webhook
s	webhooks:list|wh:list	List all the registered webhooks
s	webhooks:listen|wh:listen	Listen a webhook for outgoing callbacks
s	webhooks:payload|wh:payload	Show the payload associated to an event callback
s	webhooks:reset|wh:reset	Reset the circuit breaker associated to the webhook
s	webhooks:topics|wh:topics	Show online documentation for supported events
s	webhooks:update|wh:update	Update an existing webhook
s	adyen_payment	Execute an action on a resource of type adyen_payments
s	adyen_payment:details	Send this attribute if you want to send additional details the payment request
s	authorization	Execute an action on a resource of type authorizations
s	authorization:capture	Send this attribute if you want to create a capture for this authorization
s	authorization:capture_amount_cents	The associated capture amount, in cents
s	authorization:void	Send this attribute if you want to create a void for this authorization
s	axerve_payment	Execute an action on a resource of type axerve_payments
s	axerve_payment:update	Send this attribute if you want to update the payment with fresh order data
s	bundle	Execute an action on a resource of type bundles
s	bundle:compute_compare_at_amount	Send this attribute if you want to compute the compare_at_amount_cents as the su
s	bundle:compute_price_amount	Send this attribute if you want to compute the price_amount_cents as the sum of
s	buy_x_pay_y_promotion	Execute an action on a resource of type buy_x_pay_y_promotions
s	buy_x_pay_y_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	buy_x_pay_y_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	capture	Execute an action on a resource of type captures
s	capture:refund	Send this attribute if you want to create a refund for this capture
s	capture:refund_amount_cents	The associated refund amount, in cents
s	checkout_com_payment	Execute an action on a resource of type checkout_com_payments
s	checkout_com_payment:details	Send this attribute if you want to send additional details the payment request (
s	checkout_com_payment:refresh	Send this attribute if you want to refresh all the pending transactions, can be
s	customer_password_reset	Execute an action on a resource of type customer_password_resets
s	customer_password_reset:reset_password_token	Send the 'reset_password_token' that you got on create when updating the custome
s	external_gateway	Execute an action on a resource of type external_gateways
s	external_gateway:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	external_promotion	Execute an action on a resource of type external_promotions
s	external_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	external_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	external_promotion:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	external_tax_calculator	Execute an action on a resource of type external_tax_calculators
s	external_tax_calculator:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	fixed_amount_promotion	Execute an action on a resource of type fixed_amount_promotions
s	fixed_amount_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	fixed_amount_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	fixed_price_promotion	Execute an action on a resource of type fixed_price_promotions
s	fixed_price_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	fixed_price_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	free_gift_promotion	Execute an action on a resource of type free_gift_promotions
s	free_gift_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	free_gift_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	free_shipping_promotion	Execute an action on a resource of type free_shipping_promotions
s	free_shipping_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	free_shipping_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	gift_card	Execute an action on a resource of type gift_cards
s	gift_card:activate	Send this attribute if you want to activate a gift card
s	gift_card:balance_change_cents	The balance change, in cents
s	gift_card:deactivate	Send this attribute if you want to deactivate a gift card
s	gift_card:purchase	Send this attribute if you want to confirm a draft gift card
s	in_stock_subscription	Execute an action on a resource of type in_stock_subscriptions
s	in_stock_subscription:activate	Send this attribute if you want to activate an inactive subscription
s	in_stock_subscription:deactivate	Send this attribute if you want to dactivate an active subscription
s	klarna_payment	Execute an action on a resource of type klarna_payments
s	klarna_payment:update	Send this attribute if you want to update the payment session with fresh order d
s	line_item	Execute an action on a resource of type line_items
s	line_item:external_price	When creating or updating a new line item, set this attribute to '1' if you want
s	line_item:reserve_stock	Send this attribute if you want to reserve the stock for the line item's skus qu
s	line_item:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	market	Execute an action on a resource of type markets
s	market:disable	Send this attribute if you want to mark this resource as disabled
s	market:enable	Send this attribute if you want to mark this resource as enabled
s	order	Execute an action on a resource of type orders
s	order_subscription	Execute an action on a resource of type order_subscriptions
s	order_subscription:activate	Send this attribute if you want to mark this subscription as active
s	order_subscription:cancel	Send this attribute if you want to mark this subscription as cancelled
s	order_subscription:deactivate	Send this attribute if you want to mark this subscription as inactive
s	order:approve	Send this attribute if you want to approve a placed order
s	order:approve_and_capture	Send this attribute if you want to approve and capture a placed order
s	order:archive	Send this attribute if you want to archive the order
s	order:authorization_amount_cents	The authorization amount, in cents
s	order:authorize	Send this attribute if you want to authorize the order's payment source
s	order:billing_address_clone_id	The id of the address that you want to clone to create the order's billing addre
s	order:billing_address_same_as_shipping	Send this attribute if you want the billing address to be cloned from the order'
s	order:cancel	Send this attribute if you want to cancel a placed order
s	order:capture	Send this attribute if you want to capture an authorized order
s	order:commit_invoice	Send this attribute if you want commit the sales tax invoice to the associated t
s	order:create_subscriptions	Send this attribute upon/after placing the order if you want to create order sub
s	order:customer_payment_source_id	The id of the customer payment source (i
s	order:nullify_payment_source	Send this attribute if you want to nullify the payment source for this order
s	order:pending	Send this attribute if you want to move a draft or placing order to pending
s	order:place	Send this attribute if you want to place the order
s	order:refresh	Send this attribute if you want to manually refresh the order
s	order:refund	Send this attribute if you want to refund a captured order
s	order:refund_invoice	Send this attribute if you want refund the sales tax invoice to the associated t
s	order:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	order:save_billing_address_to_customer_address_book	Send this attribute if you want the order's billing address to be saved in the c
s	order:save_payment_source_to_customer_wallet	Send this attribute if you want the order's payment source to be saved in the cu
s	order:save_shipping_address_to_customer_address_book	Send this attribute if you want the order's shipping address to be saved in the
s	order:shipping_address_clone_id	The id of the address that you want to clone to create the order's shipping addr
s	order:shipping_address_same_as_billing	Send this attribute if you want the shipping address to be cloned from the order
s	order:start_editing	Send this attribute if you want to edit the order after it is placed
s	order:stop_editing	Send this attribute to stop the editing for the order and return back to placed
s	order:unarchive	Send this attribute if you want to unarchive the order
s	order:update_taxes	Send this attribute if you want to force tax calculation for this order (a tax c
s	order:validate	Send this attribute if you want to trigger the external validation for the order
s	payment_method	Execute an action on a resource of type payment_methods
s	payment_method:disable	Send this attribute if you want to mark this resource as disabled
s	payment_method:enable	Send this attribute if you want to mark this resource as enabled
s	percentage_discount_promotion	Execute an action on a resource of type percentage_discount_promotions
s	percentage_discount_promotion:disable	Send this attribute if you want to mark this resource as disabled
s	percentage_discount_promotion:enable	Send this attribute if you want to mark this resource as enabled
s	return	Execute an action on a resource of type returns
s	return_line_item	Execute an action on a resource of type return_line_items
s	return_line_item:restock	Send this attribute if you want to restock the line item
s	return:approve	Send this attribute if you want to mark this return as approved
s	return:archive	Send this attribute if you want to archive the return
s	return:cancel	Send this attribute if you want to mark this return as cancelled
s	return:receive	Send this attribute if you want to mark this return as received
s	return:reject	Send this attribute if you want to mark this return as rejected
s	return:request	Send this attribute if you want to activate this return
s	return:restock	Send this attribute if you want to restock all of the return line items
s	return:ship	Send this attribute if you want to mark this return as shipped
s	return:unarchive	Send this attribute if you want to unarchive the return
s	satispay_payment	Execute an action on a resource of type satispay_payments
s	satispay_payment:refresh	Send this attribute if you want to refresh all the pending transactions, can be
s	shipment	Execute an action on a resource of type shipments
s	shipment:decrement_stock	Send this attribute if you want to automatically decrement and release the stock
s	shipment:get_rates	Send this attribute if you want get the shipping rates from the associated carri
s	shipment:on_hold	Send this attribute if you want to put this shipment on hold
s	shipment:packing	Send this attribute if you want to start packing this shipment
s	shipment:picking	Send this attribute if you want to start picking this shipment
s	shipment:purchase	Send this attribute if you want to purchase this shipment with the selected rate
s	shipment:ready_to_ship	Send this attribute if you want to mark this shipment as ready to ship
s	shipment:release_stock	Send this attribute if you want to automatically destroy the stock reservations
s	shipment:reserve_stock	Send this attribute if you want to automatically reserve the stock for each of t
s	shipment:ship	Send this attribute if you want to mark this shipment as shipped
s	shipment:upcoming	Send this attribute if you want to mark this shipment as upcoming
s	shipping_method	Execute an action on a resource of type shipping_methods
s	shipping_method:disable	Send this attribute if you want to mark this resource as disabled
s	shipping_method:enable	Send this attribute if you want to mark this resource as enabled
s	shipping_method:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	stock_item	Execute an action on a resource of type stock_items
s	stock_item:validate	Send this attribute if you want to validate the stock item quantity against the
s	stock_line_item	Execute an action on a resource of type stock_line_items
s	stock_line_item:decrement_stock	Send this attribute if you want to automatically decrement and release the stock
s	stock_line_item:release_stock	Send this attribute if you want to automatically destroy the stock reservation f
s	stock_line_item:reserve_stock	Send this attribute if you want to automatically reserve the stock for this stoc
s	stock_reservation	Execute an action on a resource of type stock_reservations
s	stock_reservation:pending	Send this attribute if you want to mark this stock reservation as pending
s	stock_transfer	Execute an action on a resource of type stock_transfers
s	stock_transfer:cancel	Send this attribute if you want to cancel this stock transfer
s	stock_transfer:complete	Send this attribute if you want to complete this stock transfer
s	stock_transfer:in_transit	Send this attribute if you want to mark this stock transfer as in transit
s	stock_transfer:on_hold	Send this attribute if you want to put this stock transfer on hold
s	stock_transfer:picking	Send this attribute if you want to start picking this stock transfer
s	stock_transfer:upcoming	Send this attribute if you want to mark this stock transfer as upcoming
s	stripe_payment	Execute an action on a resource of type stripe_payments
s	stripe_payment:refresh	Send this attribute if you want to refresh the payment status, can be used as we
s	stripe_payment:update	Send this attribute if you want to update the created payment intent with fresh
s	webhook	Execute an action on a resource of type webhooks
s	webhook:disable	Send this attribute if you want to mark this resource as disabled
s	webhook:enable	Send this attribute if you want to mark this resource as enabled
s	webhook:reset_circuit	Send this attribute if you want to reset the circuit breaker associated to this
s	exports	List all the created exports or show details of a single export
s	exports:all|exp:all|export	Export all the records
s	exports:create|exp:create	Create a new export
s	exports:details|exp:details	Show the details of an existing export
s	exports:group|exp:group	List all the exports related to an export group
s	exports:list|exp:list	List all the created exports
s	exports:types|exp:types	Show online documentation for supported resources
s	cleanups	List all the created cleanups or show details of a single cleanup
s	cleanups:create|clp:create|cleanup	Create a new cleanup
s	cleanups:details|clp:details	Show the details of an existing cleanup
s	cleanups:group|clp:group	List all the cleanups related to a cleanup group
s	cleanups:list|clp:list	List all the created cleanups
s	cleanups:types|clp:types	Show online documentation for supported resources
s	provisioning:create|prov:create|pc|pcreate	Create a new resource
s	provisioning:delete|prov:delete|pd|pdelete|pdel	Delete an existing resource
s	provisioning:exec|prov:exec|pe|pexec	Execute an action on a resource
s	provisioning:fetch|prov:fetch|pf	Retrieve a resource or list a set of resources
s	provisioning:get|prov:get|pg|pget	Retrieve a resource or list a set of resources
s	provisioning:list|pl|prov:list|plist|pls	Fetch a collection of resources
s	provisioning:rel|prov:rel|prov:relationship	Fetch a resource relationship
s	provisioning:resources|prov:resources|pres	List all the available provisioning api resources
s	provisioning:retrieve|prov:retrieve|pr|pretrieve	Fetch a single resource
s	provisioning:update|prov:update|pu|pupdate|pupd	Update an existing resource
s	tags	List all the created tags or show details of a single tag
s	tags:add|tag	Add one or more tags to a set of resources
s	tags:count	Count resources tagged with a specific tag
s	tags:create	Create one or more new tags
s	tags:delete	Delete one or more existing tags
s	tags:details	Show the details of an existing tag
s	tags:list	List all the created tags
s	tags:remove	Remove one or more tags to a set of resources
s	tags:types	Show online documentation for supported resources
s	tags:update	Update an existing tag
s	tags:which	Show all the resources with this tag
s	autocomplete	Display autocomplete installation instructions
s	help	Display help for <%= config.bin %>
s	plugins	List installed plugins
s	plugins:inspect	Displays installation properties of a plugin
s	plugins:install|plugins:add	Uses bundled npm executable to install plugins into <%= config
s	plugins:link	Links a plugin into the cli for development
s	plugins:reset	
s	plugins:uninstall|plugins:unlink|plugins:remove	Removes a plugin from the cli
s	plugins:update	Update installed plugins
@	applications
o	-o|--organization	Organization slug	v
o	-k|--kind	Application kind	v
o	-m|--mode	Execution mode	v
o	--live	Live execution mode	
o	--id	Application id	v
o	-a|--alias	The alias associated to the application	v
o	-A|--api	Specific api application	v
o	-S|--sort	Sort applications by organization and application name	
=	applications	-k
v	integration	
v	sales_channel	
v	user	
=	applications	-m
v	test	
v	live	
=	applications	-A
v	core	
v	provisioning	
@	applications:add
o	-o|--organization	Organization slug	v
o	-i|--clientId	Application client_id	v
o	-s|--clientSecret	Application client_secret	v
o	-S|--scope	Access token scope (market, stock location)	v
o	-e|--email	Customer email	v
o	-p|--password	Customer secret password	v
o	-a|--alias	The alias you want to associate to the application	v
@	applications:current
o	-j|--json	Show info in json format	
@	applications:info
o	-o|--organization	Organization slug	v
o	-k|--kind	Application kind	v
o	-m|--mode	Execution mode	v
o	--live	Live execution mode	
o	--id	Application id	v
o	-a|--alias	The alias associated to the application	v
o	-A|--api	Specific api application	v
o	-j|--json	Show info in json format	
=	applications:info	-k
v	integration	
v	sales_channel	
v	user	
=	applications:info	-m
v	test	
v	live	
=	applications:info	-A
v	core	
v	provisioning	
@	applications:login
o	-o|--organization	Organization slug	v
o	-i|--clientId	Application client_id	v
o	-s|--clientSecret	Application client_secret	v
o	-S|--scope	Access token scope (market, stock location)	v
o	-e|--email	Customer email	v
o	-p|--password	Customer secret password	v
o	-a|--alias	The alias you want to associate to the application	v
@	applications:logout
o	-o|--organization	Organization slug	v
o	-k|--kind	Application kind	v
o	-m|--mode	Execution mode	v
o	--live	Live execution mode	
o	--id	Application id	v
o	-a|--alias	The alias associated to the application	v
o	-A|--api	Specific api application	v
o	-r|--revoke	Revoke current access token	
=	applications:logout	-k
v	integration	
v	sales_channel	
v	user	
=	applications:logout	-m
v	test	
v	live	
=	applications:logout	-A
v	core	
v	provisioning	
@	applications:provisioning
o	-o|--organization	Organization slug	v
o	-k|--kind	Application kind	v
o	-m|--mode	Execution mode	v
o	--live	Live execution mode	
o	--id	Application id	v
o	-a|--alias	The alias associated to the application	v
o	-A|--api	Specific api application	v
o	-S|--sort	Sort applications by organization and application name	
=	applications:provisioning	-k
v	integration	
v	sales_channel	
v	user	
=	applications:provisioning	-m
v	test	
v	live	
=	applications:provisioning	-A
v	core	
v	provisioning	
@	applications:scope
o	-a|--alias	The alias you want to associate to the application	v
a	1	0
@	applications:switch
o	-o|--organization	Organization slug	v
o	-k|--kind	Application kind	v
o	-m|--mode	Execution mode	v
o	--live	Live execution mode	
o	--id	Application id	v
o	-a|--alias	The alias associated to the application	v
o	-A|--api	Specific api application	v
=	applications:switch	-k
v	integration	
v	sales_channel	
v	user	
=	applications:switch	-m
v	test	
v	live	
=	applications:switch	-A
v	core	
v	provisioning	
@	app:token
o	-o|--organization	Organization slug	v
o	-k|--kind	Application kind	v
o	-m|--mode	Execution mode	v
o	--live	Live execution mode	
o	--id	Application id	v
o	-a|--alias	The alias associated to the application	v
o	-A|--api	Specific api application	v
o	-s|--save	Save access token	
o	-i|--info	Show access token info	
=	app:token	-k
v	integration	
v	sales_channel	
v	user	
=	app:token	-m
v	test	
v	live	
=	app:token	-A
v	core	
v	provisioning	
@	cli:update
o	-v|--version	Update cli to a specific version or tag	v
@	cli:version
o	-p|--plugins	Show version of installed plugins	
@	plugins:available
@	plugins:latest
o	-b|--beta	Retrieve latest version from beta channel	
a	1	0
@	checkout
o	-a|--accessToken	Custom access token to use instead of the one used for login	v
o	--open	Open checkout url in default browser	
o	-O|--order	An order id	v
o	-S|--sku	An sku code	v
o	-B|--bundle	A bundle code	v
o	-m|--market	A market number	v
o	-c|--coupon	A promo code	v
o	-e|--email	A customer email	v
@	checkout:order
o	-a|--accessToken	Custom access token to use instead of the one used for login	v
o	--open	Open checkout url in default browser	
a	1	0
@	imports
o	-A|--all	Show all imports instead of first 25 only	
o	-t|--type	The type of resource imported	v
o	-g|--group	The group id associated to the import in case of multi-chunk imports	v
o	-s|--status	The import job status	v
o	-e|--errors	Show only imports with errors	
o	-w|--warnings	Show only import with warnings	
o	-l|--limit	Limit number of imports in output	v
a	1	0
=	imports	-t
v	addresses	
v	bundles	
v	coupons	
v	customer_addresses	
v	customer_payment_sources	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	line_item_options	
v	orders	
v	price_tiers	
v	prices	
v	shipping_categories	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
=	imports	-s
v	in_progress	
v	pending	
v	completed	
v	interrupted	
@	imports:create
o	-t|--type	The type of resource being imported	v
o	-p|--parent	The id of the parent resource to be associated with imported data	v
o	-i|--inputs	The path of the file containing the data to import	v
o	-C|--csv	Accept input file in csv format	
o	-D|--delimiter	The delimiter character used in the csv input file (one of ',', ';', '|', tab)	v
o	-b|--blind	Execute in blind mode without showing the progress monitor	
o	-q|--quiet	Execute command without showing warning messages	
=	imports:create	-t
v	addresses	
v	bundles	
v	coupons	
v	customer_addresses	
v	customer_payment_sources	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	line_item_options	
v	orders	
v	price_tiers	
v	prices	
v	shipping_categories	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
=	imports:create	-D
v	,	
v	;	
v	|	
v	TAB	
@	imports:delete
a	1	0
@	imports:details
o	-i|--inputs	Show input items associated with the import	
o	-l|--logs	Show warning and error logs related to the import process	
o	-S|--save-inputs	Save import inputs to local file	v
a	1	0
@	imports:group
a	1	0
@	imports:list
o	-A|--all	Show all imports instead of first 25 only	
o	-t|--type	The type of resource imported	v
o	-g|--group	The group id associated to the import in case of multi-chunk imports	v
o	-s|--status	The import job status	v
o	-e|--errors	Show only imports with errors	
o	-w|--warnings	Show only import with warnings	
o	-l|--limit	Limit number of imports in output	v
=	imports:list	-t
v	addresses	
v	bundles	
v	coupons	
v	customer_addresses	
v	customer_payment_sources	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	line_item_options	
v	orders	
v	price_tiers	
v	prices	
v	shipping_categories	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
=	imports:list	-s
v	in_progress	
v	pending	
v	completed	
v	interrupted	
@	imports:types
o	-O|--open	Open online documentation page	
@	microstore
o	-a|--accessToken		v
o	--open	Open microstore url in default browser	
o	-S|--skuListId	The sku list id	v
o	-A|--all	Activate the buy all button	
o	-C|--cart	Activate the cart application	
o	-I|--inline	Disable redirect to cart application	
@	seeder:check
o	-b|--businessModel	The kind of business model you want to import	v
o	-u|--url	Seeder data url	v
o	-n|--name	The name of the business model file to use	v
o	-r|--relationships	Check resource relationships	
=	seeder:check	-b
v	single_sku	
v	multi_market	
v	custom	
@	seeder:clean
o	-b|--businessModel	The kind of business model you want to import	v
o	-u|--url	Seeder data url	v
o	-n|--name	The name of the business model file to use	v
=	seeder:clean	-b
v	single_sku	
v	multi_market	
v	custom	
@	seeder:seed
o	-b|--businessModel	The kind of business model you want to import	v
o	-u|--url	Seeder data url	v
o	-n|--name	The name of the business model file to use	v
o	-k|--keep	Keep existing resources without updating them	
=	seeder:seed	-b
v	single_sku	
v	multi_market	
v	custom	
@	token:decode
a	1	0
@	token:generate
o	-i|--info	Print generated token info	
o	-c|--check	Check generated access token	
@	token:get
o	-o|--organization	The slug of your organization	v
o	-i|--clientId	Application client_id	v
o	-s|--clientSecret	Application client_secret	v
o	-S|--scope	Access token scope (market, stock location)	v
o	-e|--email	Customer email	v
o	-p|--password	Customer secret password	v
o	--info	Show access token info	
o	-P|--provisioning	Execute login to provisioning api	
@	token:revoke
o	-o|--organization	The slug of your organization	v
o	-i|--clientId	Application client_id	v
o	-s|--clientSecret	Application client_secret	v
o	-S|--scope	Access token scope	v
o	-P|--provisioning	Execute login to provisioning api	
a	1	0
@	resources
o	-h|--help	Show cli help	
@	resources:all
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-w|--where	Comma separated list of query filters	v
o	-s|--sort	Defines results ordering	v
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-C|--csv	Export fields in csv format	
o	-D|--delimiter		v
o	-H|--header		v
o	-b|--blind	Execute in blind mode without prompt and progress bar	
o	-e|--extract	Extract subfields from object attributes	v
a	1	0
=	resources:all	-l
v	curl	
v	node	
=	resources:all	-D
v	,	
v	;	
v	|	
v	TAB	
@	resources:args
o	-a|--alias	The alias associated to saved command arguments	v
o	-r|--resource	The resource type	v
o	-o|--operation	The resource operation	v
o	-D|--delete	Delete saved arguments associated to the alias	
=	resources:args	-o
v	list	
v	retrieve	
v	create	
v	update	
@	resources:count
o	-w|--where	Comma separated list of query filters	v
a	1	0
@	resources:create
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-a|--attribute	Define a resource attribute	v
o	-O|--object	Define a resource object attribute	v
o	-r|--relationship	Define a relationship with another resource	v
o	-m|--metadata	Define a metadata attribute or a set of metadata attributes	v
o	-D|--data	The data file to use as request body	v
o	-t|--tags	List of tags associated with the resource	v
a	1	0
=	resources:create	-l
v	curl	
v	node	
#	resources:create	1
v	address	
v	adjustment	
v	adyen_gateway	
v	adyen_payment	
v	attachment	
v	avalara_account	
v	axerve_gateway	
v	axerve_payment	
v	billing_info_validation_rule	
v	bing_geocoder	
v	braintree_gateway	
v	braintree_payment	
v	bundle	
v	buy_x_pay_y_promotion	
v	checkout_com_gateway	
v	checkout_com_payment	
v	cleanup	
v	coupon	
v	coupon_codes_promotion_rule	
v	coupon_recipient	
v	credit_card	
v	custom_promotion_rule	
v	customer	
v	customer_address	
v	customer_group	
v	customer_password_reset	
v	customer_payment_source	
v	customer_subscription	
v	delivery_lead_time	
v	export	
v	external_gateway	
v	external_payment	
v	external_promotion	
v	external_tax_calculator	
v	fixed_amount_promotion	
v	fixed_price_promotion	
v	free_gift_promotion	
v	free_shipping_promotion	
v	gift_card	
v	gift_card_recipient	
v	google_geocoder	
v	import	
v	in_stock_subscription	
v	inventory_model	
v	inventory_return_location	
v	inventory_stock_location	
v	klarna_gateway	
v	klarna_payment	
v	line_item	
v	line_item_option	
v	manual_gateway	
v	manual_tax_calculator	
v	market	
v	merchant	
v	order	
v	order_amount_promotion_rule	
v	order_copy	
v	order_subscription	
v	order_subscription_item	
v	package	
v	parcel	
v	parcel_line_item	
v	payment_method	
v	payment_option	
v	paypal_gateway	
v	paypal_payment	
v	percentage_discount_promotion	
v	price	
v	price_frequency_tier	
v	price_list	
v	price_volume_tier	
v	recurring_order_copy	
v	return	
v	return_line_item	
v	satispay_gateway	
v	satispay_payment	
v	shipment	
v	shipping_category	
v	shipping_method	
v	shipping_weight_tier	
v	shipping_zone	
v	sku	
v	sku_list	
v	sku_list_item	
v	sku_list_promotion_rule	
v	sku_option	
v	spreedly_gateway	
v	stock_item	
v	stock_line_item	
v	stock_location	
v	stock_reservation	
v	stock_transfer	
v	stripe_gateway	
v	stripe_payment	
v	subscription_model	
v	tag	
v	tax_category	
v	tax_rule	
v	taxjar_account	
v	webhook	
v	wire_transfer	
@	resources:delete
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
a	2	0
=	resources:delete	-l
v	curl	
v	node	
#	resources:delete	1
v	address	
v	adjustment	
v	adyen_gateway	
v	adyen_payment	
v	attachment	
v	avalara_account	
v	axerve_gateway	
v	axerve_payment	
v	billing_info_validation_rule	
v	bing_geocoder	
v	braintree_gateway	
v	braintree_payment	
v	bundle	
v	buy_x_pay_y_promotion	
v	checkout_com_gateway	
v	checkout_com_payment	
v	cleanup	
v	coupon	
v	coupon_codes_promotion_rule	
v	coupon_recipient	
v	credit_card	
v	custom_promotion_rule	
v	customer	
v	customer_address	
v	customer_group	
v	customer_password_reset	
v	customer_payment_source	
v	customer_subscription	
v	delivery_lead_time	
v	export	
v	external_gateway	
v	external_payment	
v	external_promotion	
v	external_tax_calculator	
v	fixed_amount_promotion	
v	fixed_price_promotion	
v	free_gift_promotion	
v	free_shipping_promotion	
v	gift_card	
v	gift_card_recipient	
v	google_geocoder	
v	import	
v	in_stock_subscription	
v	inventory_model	
v	inventory_return_location	
v	inventory_stock_location	
v	klarna_gateway	
v	klarna_payment	
v	line_item	
v	line_item_option	
v	manual_gateway	
v	manual_tax_calculator	
v	market	
v	merchant	
v	order	
v	order_amount_promotion_rule	
v	order_copy	
v	order_subscription	
v	order_subscription_item	
v	package	
v	parcel	
v	parcel_line_item	
v	payment_method	
v	payment_option	
v	paypal_gateway	
v	paypal_payment	
v	percentage_discount_promotion	
v	price	
v	price_frequency_tier	
v	price_list	
v	price_volume_tier	
v	recurring_order_copy	
v	return	
v	return_line_item	
v	satispay_gateway	
v	satispay_payment	
v	shipment	
v	shipping_category	
v	shipping_method	
v	shipping_weight_tier	
v	shipping_zone	
v	sku	
v	sku_list	
v	sku_list_item	
v	sku_list_promotion_rule	
v	sku_option	
v	spreedly_gateway	
v	stock_item	
v	stock_line_item	
v	stock_location	
v	stock_reservation	
v	stock_transfer	
v	stripe_gateway	
v	stripe_payment	
v	subscription_model	
v	tag	
v	tax_category	
v	tax_rule	
v	taxjar_account	
v	webhook	
v	wire_transfer	
@	resources:doc
o	-p|--page	The doc page you want to access	v
a	1	0
=	resources:doc	-p
v	object	
v	create	
v	retrieve	
v	list	
v	update	
v	delete	
@	resources:fetch
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-e|--extract	Extract subfields from object attributes	v
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
a	2	0
=	resources:fetch	-l
v	curl	
v	node	
@	resources:filters
@	resources:get
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-e|--extract	Extract subfields from object attributes	v
a	2	0
=	resources:get	-l
v	curl	
v	node	
@	resources:list
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-e|--extract	Extract subfields from object attributes	v
a	1	0
=	resources:list	-l
v	curl	
v	node	
#	resources:list	1
v	addresses	
v	adjustments	
v	adyen_gateways	
v	adyen_payments	
v	attachments	
v	authorizations	
v	avalara_accounts	
v	axerve_gateways	
v	axerve_payments	
v	billing_info_validation_rules	
v	bing_geocoders	
v	braintree_gateways	
v	braintree_payments	
v	bundles	
v	buy_x_pay_y_promotions	
v	captures	
v	carrier_accounts	
v	checkout_com_gateways	
v	checkout_com_payments	
v	cleanups	
v	coupons	
v	coupon_codes_promotion_rules	
v	coupon_recipients	
v	credit_cards	
v	custom_promotion_rules	
v	customers	
v	customer_addresses	
v	customer_groups	
v	customer_password_resets	
v	customer_payment_sources	
v	customer_subscriptions	
v	delivery_lead_times	
v	events	
v	event_callbacks	
v	exports	
v	external_gateways	
v	external_payments	
v	external_promotions	
v	external_tax_calculators	
v	fixed_amount_promotions	
v	fixed_price_promotions	
v	free_gift_promotions	
v	free_shipping_promotions	
v	geocoders	
v	gift_cards	
v	gift_card_recipients	
v	google_geocoders	
v	imports	
v	in_stock_subscriptions	
v	inventory_models	
v	inventory_return_locations	
v	inventory_stock_locations	
v	klarna_gateways	
v	klarna_payments	
v	line_items	
v	line_item_options	
v	manual_gateways	
v	manual_tax_calculators	
v	markets	
v	merchants	
v	orders	
v	order_amount_promotion_rules	
v	order_copies	
v	order_factories	
v	order_subscriptions	
v	order_subscription_items	
v	order_validation_rules	
v	packages	
v	parcels	
v	parcel_line_items	
v	payment_gateways	
v	payment_methods	
v	payment_options	
v	paypal_gateways	
v	paypal_payments	
v	percentage_discount_promotions	
v	prices	
v	price_frequency_tiers	
v	price_lists	
v	price_tiers	
v	price_volume_tiers	
v	promotions	
v	promotion_rules	
v	recurring_order_copies	
v	refunds	
v	reserved_stocks	
v	resource_errors	
v	returns	
v	return_line_items	
v	satispay_gateways	
v	satispay_payments	
v	shipments	
v	shipment_line_items	
v	shipping_categories	
v	shipping_methods	
v	shipping_method_tiers	
v	shipping_weight_tiers	
v	shipping_zones	
v	skus	
v	sku_lists	
v	sku_list_items	
v	sku_list_promotion_rules	
v	sku_options	
v	spreedly_gateways	
v	stock_items	
v	stock_line_items	
v	stock_locations	
v	stock_reservations	
v	stock_transfers	
v	stripe_gateways	
v	stripe_payments	
v	subscription_models	
v	tags	
v	tax_calculators	
v	tax_categories	
v	tax_rules	
v	taxjar_accounts	
v	transactions	
v	versions	
v	voids	
v	webhooks	
v	wire_transfers	
@	relationship
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-e|--extract	Extract subfields from object attributes	v
a	3	0
=	relationship	-l
v	curl	
v	node	
@	resources:retrieve
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-e|--extract	Extract subfields from object attributes	v
a	2	0
=	resources:retrieve	-l
v	curl	
v	node	
#	resources:retrieve	1
v	address	
v	adjustment	
v	adyen_gateway	
v	adyen_payment	
v	application	
v	attachment	
v	authorization	
v	avalara_account	
v	axerve_gateway	
v	axerve_payment	
v	billing_info_validation_rule	
v	bing_geocoder	
v	braintree_gateway	
v	braintree_payment	
v	bundle	
v	buy_x_pay_y_promotion	
v	capture	
v	carrier_account	
v	checkout_com_gateway	
v	checkout_com_payment	
v	cleanup	
v	coupon	
v	coupon_codes_promotion_rule	
v	coupon_recipient	
v	credit_card	
v	custom_promotion_rule	
v	customer	
v	customer_address	
v	customer_group	
v	customer_password_reset	
v	customer_payment_source	
v	customer_subscription	
v	delivery_lead_time	
v	event	
v	event_callback	
v	export	
v	external_gateway	
v	external_payment	
v	external_promotion	
v	external_tax_calculator	
v	fixed_amount_promotion	
v	fixed_price_promotion	
v	free_gift_promotion	
v	free_shipping_promotion	
v	geocoder	
v	gift_card	
v	gift_card_recipient	
v	google_geocoder	
v	import	
v	in_stock_subscription	
v	inventory_model	
v	inventory_return_location	
v	inventory_stock_location	
v	klarna_gateway	
v	klarna_payment	
v	line_item	
v	line_item_option	
v	manual_gateway	
v	manual_tax_calculator	
v	market	
v	merchant	
v	order	
v	order_amount_promotion_rule	
v	order_copy	
v	order_factory	
v	order_subscription	
v	order_subscription_item	
v	order_validation_rule	
v	organization	
v	package	
v	parcel	
v	parcel_line_item	
v	payment_gateway	
v	payment_method	
v	payment_option	
v	paypal_gateway	
v	paypal_payment	
v	percentage_discount_promotion	
v	price	
v	price_frequency_tier	
v	price_list	
v	price_tier	
v	price_volume_tier	
v	promotion	
v	promotion_rule	
v	recurring_order_copy	
v	refund	
v	reserved_stock	
v	resource_error	
v	return	
v	return_line_item	
v	satispay_gateway	
v	satispay_payment	
v	shipment	
v	shipment_line_item	
v	shipping_category	
v	shipping_method	
v	shipping_method_tier	
v	shipping_weight_tier	
v	shipping_zone	
v	sku	
v	sku_list	
v	sku_list_item	
v	sku_list_promotion_rule	
v	sku_option	
v	spreedly_gateway	
v	stock_item	
v	stock_line_item	
v	stock_location	
v	stock_reservation	
v	stock_transfer	
v	stripe_gateway	
v	stripe_payment	
v	subscription_model	
v	tag	
v	tax_calculator	
v	tax_category	
v	tax_rule	
v	taxjar_account	
v	transaction	
v	version	
v	void	
v	webhook	
v	wire_transfer	
@	resources:schema
@	resources:update
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	--save-args	Save command data to file for future use	v
o	--load-args	Load previously saved command arguments	v
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-a|--attribute	Define a resource attribute	v
o	-O|--object	Define a resource object attribute	v
o	-r|--relationship	Define a relationship with another resource	v
o	-m|--metadata		v
o	-M|--metadata-replace		v
o	-D|--data	The data file to use as request body	v
o	-t|--tags	List of tags associated with the resource	v
a	2	0
=	resources:update	-l
v	curl	
v	node	
#	resources:update	1
v	address	
v	adjustment	
v	adyen_gateway	
v	adyen_payment	
v	attachment	
v	authorization	
v	avalara_account	
v	axerve_gateway	
v	axerve_payment	
v	billing_info_validation_rule	
v	bing_geocoder	
v	braintree_gateway	
v	braintree_payment	
v	bundle	
v	buy_x_pay_y_promotion	
v	capture	
v	checkout_com_gateway	
v	checkout_com_payment	
v	coupon	
v	coupon_codes_promotion_rule	
v	coupon_recipient	
v	credit_card	
v	custom_promotion_rule	
v	customer	
v	customer_address	
v	customer_group	
v	customer_password_reset	
v	customer_payment_source	
v	customer_subscription	
v	delivery_lead_time	
v	external_gateway	
v	external_payment	
v	external_promotion	
v	external_tax_calculator	
v	fixed_amount_promotion	
v	fixed_price_promotion	
v	free_gift_promotion	
v	free_shipping_promotion	
v	gift_card	
v	gift_card_recipient	
v	google_geocoder	
v	in_stock_subscription	
v	inventory_model	
v	inventory_return_location	
v	inventory_stock_location	
v	klarna_gateway	
v	klarna_payment	
v	line_item	
v	line_item_option	
v	manual_gateway	
v	manual_tax_calculator	
v	market	
v	merchant	
v	order	
v	order_amount_promotion_rule	
v	order_copy	
v	order_subscription	
v	order_subscription_item	
v	package	
v	parcel	
v	parcel_line_item	
v	payment_method	
v	payment_option	
v	paypal_gateway	
v	paypal_payment	
v	percentage_discount_promotion	
v	price	
v	price_frequency_tier	
v	price_list	
v	price_volume_tier	
v	recurring_order_copy	
v	return	
v	return_line_item	
v	satispay_gateway	
v	satispay_payment	
v	shipment	
v	shipping_category	
v	shipping_method	
v	shipping_weight_tier	
v	shipping_zone	
v	sku	
v	sku_list	
v	sku_list_item	
v	sku_list_promotion_rule	
v	sku_option	
v	spreedly_gateway	
v	stock_item	
v	stock_line_item	
v	stock_location	
v	stock_reservation	
v	stock_transfer	
v	stripe_gateway	
v	stripe_payment	
v	subscription_model	
v	tag	
v	tax_category	
v	tax_rule	
v	taxjar_account	
v	webhook	
v	wire_transfer	
@	orders
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:approve
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:approve_and_capture
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:archive
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:authorization_amount_cents
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:authorize
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:billing_address_clone_id
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
o	-v|--value	The trigger attribute value	v
a	1	0
@	orders:billing_address_same_as_shipping
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:cancel
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:capture
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:commit_invoice
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:create_subscriptions
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:customer_payment_source_id
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
o	-v|--value	The trigger attribute value	v
a	1	0
@	orders:nullify_payment_source
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:pending
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:place
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:refresh
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:refund
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:refund_invoice
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:reset_circuit
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:save_billing_address_to_customer_address_book
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:save_payment_source_to_customer_wallet
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:save_shipping_address_to_customer_address_book
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:shipping_address_clone_id
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
o	-v|--value	The trigger attribute value	v
a	1	0
@	orders:shipping_address_same_as_billing
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:start_editing
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:stop_editing
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:unarchive
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:update_taxes
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	orders:validate
o	-p|--print	Print out the modified order	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	webhooks
o	-c|--circuit	Show only webhooks with circuit in the declared state	v
o	-t|--topic	The event that triggered the webhook	v
o	-H|--hide-empty	Hide empty attributes	
o	-e|--events	Show the last event callbacks associated to the webhook	
a	1	0
=	webhooks	-c
v	open	
v	closed	
@	webhooks:create
o	-t|--topic	The identifier of the event that will trigger the webhook	v
o	-u|--url	The callback url used to post data	v
o	-i|--include	A comma separated list of related resources to be included	v
o	-n|--name	The webhook short name	v
@	webhooks:destroy
a	1	0
@	webhooks:details
o	-H|--hide-empty	Hide empty attributes	
o	-e|--events	Show the last event callbacks associated to the webhook	
a	1	0
@	webhooks:event
o	-p|--payload	Show the event payload sent to the callback endpoint	
o	-f|--format	Format the payload output	
a	1	0
@	webhooks:events
o	-A|--all	Show all events instead of first 25 only	
o	-l|--limit	Limit number of events in output	v
a	1	0
@	webhooks:list
o	-c|--circuit	Show only webhooks with circuit in the declared state	v
o	-t|--topic	The event that triggered the webhook	v
=	webhooks:list	-c
v	open	
v	closed	
@	webhooks:listen
o	-t|--time	Waiting time for the first event	v
a	1	0
@	webhooks:payload
o	-f|--format	Format the payload output	
a	1	0
@	webhooks:reset
a	1	0
@	webhooks:topics
@	webhooks:update
o	-t|--topic	The identifier of the event that will trigger the webhook	v
o	-u|--url	The callback url used to post data	v
o	-i|--include	A comma separated list of related resources to be included	v
o	-n|--name	The webhook short name	v
a	1	0
@	adyen_payment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	adyen_payment:details
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	authorization
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	authorization:capture
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	authorization:capture_amount_cents
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	authorization:void
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	axerve_payment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	axerve_payment:update
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	bundle
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	bundle:compute_compare_at_amount
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	bundle:compute_price_amount
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	buy_x_pay_y_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	buy_x_pay_y_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	buy_x_pay_y_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	capture
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	capture:refund
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	capture:refund_amount_cents
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	checkout_com_payment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	checkout_com_payment:details
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	checkout_com_payment:refresh
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	customer_password_reset
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	customer_password_reset:reset_password_token
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_gateway
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_gateway:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_promotion:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_tax_calculator
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	external_tax_calculator:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	fixed_amount_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	fixed_amount_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	fixed_amount_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	fixed_price_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	fixed_price_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	fixed_price_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	free_gift_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	free_gift_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	free_gift_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	free_shipping_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	free_shipping_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	free_shipping_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	gift_card
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	gift_card:activate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	gift_card:balance_change_cents
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	gift_card:deactivate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	gift_card:purchase
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	in_stock_subscription
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	in_stock_subscription:activate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	in_stock_subscription:deactivate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	klarna_payment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	klarna_payment:update
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	line_item
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	line_item:external_price
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	line_item:reserve_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	line_item:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	market
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	market:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	market:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order_subscription
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order_subscription:activate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order_subscription:cancel
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order_subscription:deactivate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:approve
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:approve_and_capture
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:archive
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:authorization_amount_cents
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:authorize
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:billing_address_clone_id
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
o	-v|--value	The trigger attribute value	v
a	1	0
@	order:billing_address_same_as_shipping
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:cancel
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:capture
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:commit_invoice
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:create_subscriptions
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:customer_payment_source_id
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
o	-v|--value	The trigger attribute value	v
a	1	0
@	order:nullify_payment_source
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:pending
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:place
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:refresh
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:refund
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:refund_invoice
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:save_billing_address_to_customer_address_book
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:save_payment_source_to_customer_wallet
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:save_shipping_address_to_customer_address_book
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:shipping_address_clone_id
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
o	-v|--value	The trigger attribute value	v
a	1	0
@	order:shipping_address_same_as_billing
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:start_editing
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:stop_editing
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:unarchive
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:update_taxes
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	order:validate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	payment_method
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	payment_method:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	payment_method:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	percentage_discount_promotion
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	percentage_discount_promotion:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	percentage_discount_promotion:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return_line_item
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return_line_item:restock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:approve
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:archive
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:cancel
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:receive
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:reject
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:request
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:restock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:ship
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	return:unarchive
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	satispay_payment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	satispay_payment:refresh
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:decrement_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:get_rates
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:on_hold
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:packing
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:picking
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:purchase
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:ready_to_ship
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:release_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:reserve_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:ship
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipment:upcoming
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipping_method
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipping_method:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipping_method:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	shipping_method:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_item
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_item:validate
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_line_item
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_line_item:decrement_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_line_item:release_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_line_item:reserve_stock
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_reservation
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_reservation:pending
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer:cancel
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer:complete
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer:in_transit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer:on_hold
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer:picking
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stock_transfer:upcoming
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stripe_payment
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stripe_payment:refresh
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	stripe_payment:update
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	webhook
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	webhook:disable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	webhook:enable
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	webhook:reset_circuit
o	-p|--print	Print out the modified resource	
o	-j|--json	Print result in json format	
o	-u|--unformatted	Print json output without indentation	
a	1	0
@	exports
o	-A|--all	Show all exports instead of first 25 only	
o	-t|--type	The type of resource exported	v
o	-s|--status	The export job status	v
o	-l|--limit	Limit number of exports in output	v
a	1	0
=	exports	-t
v	addresses	
v	authorizations	
v	bundles	
v	captures	
v	coupons	
v	customer_addresses	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	orders	
v	payment_methods	
v	price_tiers	
v	prices	
v	refunds	
v	shipments	
v	shipping_categories	
v	shipping_methods	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
v	transactions	
v	voids	
=	exports	-s
v	in_progress	
v	pending	
v	completed	
v	interrupted	
@	exports:all
o	-t|--type	The type of resource being exported	v
o	-i|--include	Comma separated resources to include	v
o	-w|--where	Comma separated list of query filters	v
o	-D|--dry-data	Skip redundant attributes	
o	-F|--format	Export file format	v
o	-C|--csv	Export data in csv format	
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-b|--blind	Execute in blind mode without showing the progress monitor	
o	-P|--prettify	Prettify json output format	
o	-O|--open	Open automatically the file after a successful export	
o	-q|--quiet	Execute command without showing warning messages	
o	-k|--keep	Keep original export files in temp dir	
=	exports:all	-t
v	addresses	
v	authorizations	
v	bundles	
v	captures	
v	coupons	
v	customer_addresses	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	orders	
v	payment_methods	
v	price_tiers	
v	prices	
v	refunds	
v	shipments	
v	shipping_categories	
v	shipping_methods	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
v	transactions	
v	voids	
=	exports:all	-F
v	csv	
v	json	
@	exports:create
o	-t|--type	The type of resource being exported	v
o	-i|--include	Comma separated resources to include	v
o	-w|--where	Comma separated list of query filters	v
o	-D|--dry-data	Skip redundant attributes	
o	-F|--format	Export file format	v
o	-C|--csv	Export data in csv format	
o	-x|--save	Save command output to file	v
o	-X|--save-path	Save command output to file and create missing path directories	v
o	-b|--blind	Execute in blind mode without showing the progress monitor	
o	-P|--prettify	Prettify json output format	
o	-O|--open	Open automatically the file after a successful export	
=	exports:create	-t
v	addresses	
v	authorizations	
v	bundles	
v	captures	
v	coupons	
v	customer_addresses	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	orders	
v	payment_methods	
v	price_tiers	
v	prices	
v	refunds	
v	shipments	
v	shipping_categories	
v	shipping_methods	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
v	transactions	
v	voids	
=	exports:create	-F
v	csv	
v	json	
@	exports:details
a	1	0
@	exports:group
a	1	0
@	exports:list
o	-A|--all	Show all exports instead of first 25 only	
o	-t|--type	The type of resource exported	v
o	-s|--status	The export job status	v
o	-l|--limit	Limit number of exports in output	v
=	exports:list	-t
v	addresses	
v	authorizations	
v	bundles	
v	captures	
v	coupons	
v	customer_addresses	
v	customer_subscriptions	
v	customers	
v	gift_cards	
v	line_items	
v	orders	
v	payment_methods	
v	price_tiers	
v	prices	
v	refunds	
v	shipments	
v	shipping_categories	
v	shipping_methods	
v	sku_lists	
v	sku_list_items	
v	sku_options	
v	skus	
v	stock_items	
v	tags	
v	tax_categories	
v	transactions	
v	voids	
=	exports:list	-s
v	in_progress	
v	pending	
v	completed	
v	interrupted	
@	exports:types
o	-O|--open	Open online documentation page	
@	cleanups
o	-A|--all	Show all cleanups instead of first 25 only	
o	-t|--type	The type of resource cleaned	v
o	-s|--status	The cleanup job status	v
o	-l|--limit	Limit number of cleanups in output	v
a	1	0
=	cleanups	-t
v	bundles	
v	gift_cards	
v	prices	
v	promotions	
v	sku_lists	
v	sku_options	
v	skus	
v	stock_items	
=	cleanups	-s
v	in_progress	
v	pending	
v	completed	
v	interrupted	
@	cleanups:create
o	-t|--type	The type of resource to clean up	v
o	-w|--where	Comma separated list of query filters	v
o	-b|--blind	Execute in blind mode without showing the progress monitor	
o	-q|--quiet	Execute command without showing warning messages	
=	cleanups:create	-t
v	bundles	
v	gift_cards	
v	prices	
v	promotions	
v	sku_lists	
v	sku_options	
v	skus	
v	stock_items	
@	cleanups:details
o	-l|--logs	Show error logs related to the cleanup process	
a	1	0
@	cleanups:group
a	1	0
@	cleanups:list
o	-A|--all	Show all cleanups instead of first 25 only	
o	-t|--type	The type of resource cleaned	v
o	-s|--status	The cleanup job status	v
o	-l|--limit	Limit number of cleanups in output	v
=	cleanups:list	-t
v	bundles	
v	gift_cards	
v	prices	
v	promotions	
v	sku_lists	
v	sku_options	
v	skus	
v	stock_items	
=	cleanups:list	-s
v	in_progress	
v	pending	
v	completed	
v	interrupted	
@	cleanups:types
o	-O|--open	Open online documentation page	
@	provisioning:create
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-a|--attribute	Define a resource attribute	v
o	-O|--object	Define a resource object attribute	v
o	-r|--relationship	Define a relationship with another resource	v
o	-m|--metadata	Define a metadata attribute or a set of metadata attributes	v
o	-D|--data	The data file to use as request body	v
a	1	0
=	provisioning:create	-l
v	curl	
v	node	
#	provisioning:create	1
v	api_credential	
v	application_membership	
v	membership	
v	organization	
v	permission	
v	role	
v	subscription	
@	provisioning:delete
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
a	2	0
=	provisioning:delete	-l
v	curl	
v	node	
#	provisioning:delete	1
v	api_credential	
v	application_membership	
v	membership	
@	provisioning:exec
o	-a|--attribute	Define a resource attribute	v
a	3	0
@	provisioning:fetch
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-e|--extract	Extract subfields from object attributes	v
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
a	3	0
=	provisioning:fetch	-l
v	curl	
v	node	
@	provisioning:get
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-e|--extract	Extract subfields from object attributes	v
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
a	2	0
=	provisioning:get	-l
v	curl	
v	node	
@	provisioning:list
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
o	-e|--extract	Extract subfields from object attributes	v
a	1	0
=	provisioning:list	-l
v	curl	
v	node	
#	provisioning:list	1
v	api_credentials	
v	application_memberships	
v	memberships	
v	organizations	
v	permissions	
v	plans	
v	roles	
v	subscriptions	
v	versions	
@	provisioning:rel
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-w|--where	Comma separated list of query filters	v
o	-p|--page	Page number	v
o	-n|--pageSize	Number of elements per page	v
o	-s|--sort	Defines results ordering	v
o	-e|--extract	Extract subfields from object attributes	v
a	3	0
=	provisioning:rel	-l
v	curl	
v	node	
@	provisioning:resources
o	-h|--help	Show cli help	
@	provisioning:retrieve
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-e|--extract	Extract subfields from object attributes	v
a	2	0
=	provisioning:retrieve	-l
v	curl	
v	node	
#	provisioning:retrieve	1
v	api_credential	
v	application_membership	
v	billing_profile	
v	membership	
v	organization	
v	permission	
v	plan	
v	role	
v	subscription	
v	user	
v	version	
@	provisioning:update
o	-i|--include	Comma separated resources to include	v
o	-f|--fields	Comma separeted list of fields in the format [resourcetype/]field1,field2,field3	v
o	-j|--json	Convert output in standard json format	
o	-u|--unformatted	Print unformatted json output	
o	-R|--raw	Print out the raw api response	
o	--doc	Show the cli command in a specific language	
o	-l|--lang	Show the cli command in the specified language syntax	v
o	--curl	Show the equivalent curl command of the cli command	
o	--node	Show the equivalent node sdk source code of the cli command	
o	-H|--headers	Show response headers	
o	-Y|--headers-only	Show only response headers	
o	-a|--attribute	Define a resource attribute	v
o	-O|--object	Define a resource object attribute	v
o	-r|--relationship	Define a relationship with another resource	v
o	-m|--metadata		v
o	-M|--metadata-replace		v
o	-D|--data	The data file to use as request body	v
a	2	0
=	provisioning:update	-l
v	curl	
v	node	
#	provisioning:update	1
v	api_credential	
v	application_membership	
v	membership	
v	organization	
v	permission	
v	role	
v	user	
@	tags
o	-A|--all	Show all tags instead of first 25 only	
o	-l|--limit	Limit number of tags in output	v
a	1	0
@	tags:add
o	-n|--name	The tag name	v
o	-t|--type	The type of the resource to tag	v
o	-i|--id	The ids of the resources to tag	v
o	-C|--create	Create tags if don't exist	v
o	-v|--verbose	Show details of the tag process	
@	tags:count
o	-t|--type	The type of the tagged resources	v
o	-z|--zero	Show also resources without tags	
a	1	0
@	tags:create
o	-n|--name	The tag name	v
@	tags:delete
o	-n|--name	The tag name	v
@	tags:details
a	1	0
@	tags:list
o	-A|--all	Show all tags instead of first 25 only	
o	-l|--limit	Limit number of tags in output	v
@	tags:remove
o	-n|--name	The tag name	v
o	-t|--type	The type of the resource to tag	v
o	-i|--id	The ids of th eresources to tag	v
o	-v|--verbose	Show details of the tag process	
@	tags:types
o	-O|--open	Open online documentation page	
@	tags:update
o	-n|--name	The new tag name	v
a	1	0
@	tags:which
o	-t|--type	The type of the tagged resources	v
o	-A|--all	Show all resources instead of first 25 only	
o	-l|--limit	Limit number of resources in output	v
a	1	0
@	autocomplete
o	-r|--refresh-cache	Refresh cache (ignores displaying instructions)	
a	1	0
#	autocomplete	1
v	zsh	
v	bash	
v	powershell	
@	help
o	-n|--nested-commands	Include all nested commands in the output	
a	1	0
@	plugins
o	--json	Format output as json	
o	--core	Show core plugins	
@	plugins:inspect
o	--json	Format output as json	
o	-h|--help	Show cli help	
o	-v|--verbose		
a	1	0
@	plugins:install
o	--json	Format output as json	
o	-f|--force	Force npm to fetch remote resources even if a local copy exists on disk	
o	-h|--help	Show cli help	
o	-s|--silent	Silences npm output	
o	-v|--verbose	Show verbose npm output	
a	1	0
@	plugins:link
o	-h|--help	Show cli help	
o	--install	Install dependencies after linking the plugin	
o	--no-install		
o	-v|--verbose		
a	1	0
@	plugins:reset
o	--hard		
o	--reinstall		
@	plugins:uninstall
o	-h|--help	Show cli help	
o	-v|--verbose		
a	1	0
@	plugins:update
o	-h|--help	Show cli help	
o	-v|--verbose		
