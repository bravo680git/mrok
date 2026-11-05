@	
s	login	Connects to your Stripe account
s	config	Installs a tool in your toolchain
s	completion	Generates shell autocompletions
s	logs tail	Logs from your Stripe requests
s	status	Displays Stripe's system status and service availability
s	open	Displays Stripe's system status and service availability
s	listen	Receives webhook events from Stripe locally
s	trigger	Triggers webhook events to conduct local testing
s	events resend	Resend an event to test a webhook endpoint
s	get	Makes GET HTTP requests to retrieve an individual API object
s	post	Makes POST HTTP requests to the Stripe API
s	delete	Makes DELETE HTTP requests to the Stripe API
s	samples	Creates a local copy of a sample
s	serve	Starts an HTTP server to serve static files
s	terminal quickstart	Starts up Stripe Terminal
s	logout	Removes all credentials
s	feedback	Prints info about how to provide feedback
s	help	Gets help for any command
s	version	Gets the version and checks or updates
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=		--color
v	on	
v	off	
v	auto	
=		--config
t	filepaths
=		--log-level
v	info	
v	debug	
v	warn	
v	error	
@	login
o	-i|--interactive	Manually provide an API key if you can't access a browser	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	1
=	login	--color
v	on	
v	off	
v	auto	
=	login	--config
t	filepaths
=	login	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	config
o	-e|--edit	Opens the configuration file in your default editor	
o	--list	List all configured options	
o	--set	Set a value for the specified configuration option	v
o	--unset	Remove a key-value pair from the config file	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	config	--color
v	on	
v	off	
v	auto	
=	config	--config
t	filepaths
=	config	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	completion
o	--shell	Opens the configuration file in your default editor	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	completion	--shell
v	zsh	
v	bash	
=	completion	--color
v	on	
v	off	
v	auto	
=	completion	--config
t	filepaths
=	completion	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	logs tail
o	--filter-account	Filters request logs by the source and destination account	v
o	--filter-http-method	Filters request logs by HTTP method	v
o	--filter-ip-address	Filters request logs by IP address	v
o	--filter-request-path	Filters request logs that directly match any Stripe path	v
o	--filter-request-status	Filters request logs by the response status	v
o	--filter-source	Filters request logs by the source of each request	v
o	--filter-status-code	Filters request logs by HTTP status code	v
o	--filter-status-code-type	Filters request logs by the type of HTTP status code	v
o	--format	Specify the output format for request logs	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	logs tail	--filter-account
v	connect_in	Incoming Connect requests
v	connect_out	Outgoing Connect requests
v	self	Non-Connect requests
=	logs tail	--filter-http-method
v	GET	HTTP GET requests
v	POST	HTTP POST requests
v	DELETE	HTTP DELETE requests
=	logs tail	--filter-request-status
v	SUCCEEDED	Requests that succeeded
v	FAILED	Requests that failed
=	logs tail	--filter-source
v	API	Requests created with the Stripe API
v	DASHBOARD	Requests created from the Dashboard
=	logs tail	--filter-status-code-type
v	2XX	HTTP 2xx status codes
v	4XX	HTTP 4xx status codes
v	5XX	HTTP 5xx status codes
=	logs tail	--format
v	JSON	Output logs in JSON format
=	logs tail	--color
v	on	
v	off	
v	auto	
=	logs tail	--config
t	filepaths
=	logs tail	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	status
o	--format	Formats used to display status	v
o	--hide-spinner	Hides the loading spinner when polling	
o	--poll	Keeps polling for status updates	
o	--poll-rate	The number of seconds (min 5) to wait between status updates	v
o	--verbose	Shows the status of all Stripe systems	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	status	--format
v	default	Render the status using standard output
v	JSON	Render status as JSON
=	status	--color
v	on	
v	off	
v	auto	
=	status	--config
t	filepaths
=	status	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	open
o	--list	Lists all supported shortcuts	
o	--live	Opens the Dashboard for your live integrations	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	open	--color
v	on	
v	off	
v	auto	
=	open	--config
t	filepaths
=	open	--log-level
v	info	
v	debug	
v	warn	
v	error	
#	open	1
v	api	
v	apiref	
v	cliref	
v	dashboard	
v	dashboard/apikeys	
v	dashboard/atlas	
v	dashboard/balance	
v	dashboard/billing	
v	dashboard/connect	
v	dashboard/connect/accounts	
v	dashboard/connect/collected	
v	dashboard/connect/transfers	
v	dashboard/coupons	
v	dashboard/customers	
v	dashboard/developers	
v	dashboard/disputes	
v	dashboard/events	
v	dashboard/invoices	
v	dashboard/logs	
v	dashboard/orders	
v	dashboard/orders/products	
v	dashboard/payments	
v	dashboard/radar	
v	dashboard/radar/list	
v	dashboard/radar/reviews	
v	dashboard/radar/rules	
v	dashboard/settings	
v	dashboard/subscriptions	
v	dashboard/products	
v	dashboard/tax	
v	dashboard/terminal	
v	dashbaord/terminal/hardware/orders	
v	dashboard/terminal/locations	
v	dashboard/topups	
v	dashboard/transactions	
v	dashboard/webhooks	
v	docs	
@	listen
o	--connect-headers	A comma-separated list of custom HTTP headers to any connected accounts	v
o	-e|--events	A comma-separated list of which events to listen for	v
o	-c|--forward-connect-to	The URL that Connect webhook events will be forwarded to	v
o	-f|--forward-to	The URL that webhook events will be forwarded to	v
o	-H|--headers	A comma-separated list of custom HTTP headers to forward	v
o	-l|--latest	Receive events used in the latest API version	
o	--live	Make a live request	
o	-a|--load-from-webhooks-api	Listen for all webhook events based on existing webhook endpoints	
o	-j|--print-json	Print JSON objects to stdout	
o	--skip-verify	Skip certificate verification when forwarding to HTTPS endpoints	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	listen	-e
v	account.updated	Occurs whenever an account status or property has changed
v	account.application.authorized	Occurs whenever a user authorizes an application. Sent to the related application only
v	account.application.deauthorized	Occurs whenever a user deauthorizes an application. Sent to the related application only
v	account.external_account.created	Occurs whenever an external account is created
v	account.external_account.deleted	Occurs whenever an external account is deleted
v	account.external_account.updated	Occurs whenever an external account is updated
v	application_fee.created	Occurs whenever an application fee is created on a charge
v	application_fee.refunded	Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding…
v	application_fee.refund.updated	Occurs whenever an application fee refund is updated
v	billing_portal.configuration.created	Occurs whenever a portal configuration is created
v	billing_portal.configuration.updated	Occurs whenever a portal configuration is updated
v	capability.updated	Occurs whenever a capability has new requirements or a new status
v	charge.expired	Occurs whenever an uncaptured charge expires
v	charge.pending	Occurs whenever a pending charge is created
v	charge.updated	Occurs whenever a charge description or metadata is updated
v	charge.dispute.closed	Occurs when a dispute is closed and the dispute status changes to lost, warning_closed, or won
v	charge.dispute.funds_reinstated	Occurs when funds are reinstated to your account after a dispute is closed. This includes…
v	charge.dispute.funds_withdrawn	Occurs when funds are removed from your account due to a dispute
v	charge.dispute.updated	Occurs when the dispute is updated (usually with evidence)
v	charge.refund.updated	Occurs whenever a refund is updated, on selected payment methods
v	checkout.session.async_payment_failed	Occurs when a payment intent using a delayed payment method fails
v	checkout.session.async_payment_succeeded	Occurs when a payment intent using a delayed payment method finally succeeds
v	coupon.created	Occurs whenever a coupon is created
v	coupon.deleted	Occurs whenever a coupon is deleted
v	coupon.updated	Occurs whenever a coupon is updated
v	credit_note.created	Occurs whenever a credit note is created
v	credit_note.updated	Occurs whenever a credit note is updated
v	credit_note.voided	Occurs whenever a credit note is voided
v	customer.discount.created	Occurs whenever a coupon is attached to a customer
v	customer.discount.deleted	Occurs whenever a coupon is removed from a customer
v	customer.discount.updated	Occurs whenever a customer is switched from one coupon to another
v	customer.source.deleted	Occurs whenever a source is removed from a customer
v	customer.source.expiring	Occurs whenever a card or source will expire at the end of the month
v	customer.subscription.pending_update_applied	Occurs whenever a customer's subscription's pending update is applied, and the subscription is…
v	customer.subscription.pending_update_expired	Occurs whenever a customer's subscription's pending update expires before the related invoice is…
v	customer.subscription.trial_will_end	Occurs three days before a subscription's trial period is scheduled to end, or when a trial is…
v	customer.tax_id.created	Occurs whenever a tax ID is created for a customer
v	customer.tax_id.deleted	Occurs whenever a tax ID is deleted from a customer
v	customer.tax_id.updated	Occurs whenever a customer's tax ID is updated
v	file.created	Occurs whenever a new Stripe-generated file is available for your account
v	identity.verification_session.canceled	Occurs whenever a VerificationSession is canceled
v	identity.verification_session.created	Occurs whenever a VerificationSession is created
v	identity.verification_session.processing	Occurs whenever a VerificationSession transitions to processing
v	identity.verification_session.redacted	Occurs whenever a VerificationSession is redacted. You must create a webhook endpoint which…
v	identity.verification_session.requires_input	Occurs whenever a VerificationSession transitions to require user input
v	identity.verification_session.verified	Occurs whenever a VerificationSession transitions to verified
v	invoice.deleted	Occurs whenever a draft invoice is deleted
v	invoice.finalization_failed	Occurs whenever a draft invoice cannot be finalized. See the invoice’s last finalization error for…
v	invoice.marked_uncollectible	Occurs whenever an invoice is marked uncollectible
v	invoice.paid	Occurs whenever an invoice payment attempt succeeds or an invoice is marked as paid out-of-band
v	invoice.payment_action_required	Occurs whenever an invoice payment attempt requires further user action to complete
v	invoice.sent	Occurs whenever an invoice email is sent out
v	invoice.upcoming	Occurs X number of days before a subscription is scheduled to create an invoice that is…
v	invoice.voided	Occurs whenever an invoice is voided
v	invoiceitem.created	Occurs whenever an invoice item is created
v	invoiceitem.deleted	Occurs whenever an invoice item is deleted
v	invoiceitem.updated	Occurs whenever an invoice item is updated
v	issuing_authorization.created	Occurs whenever an authorization is created
v	issuing_authorization.updated	Occurs whenever an authorization is updated
v	issuing_card.updated	Occurs whenever a card is updated
v	issuing_cardholder.updated	Occurs whenever a cardholder is updated
v	issuing_dispute.closed	Occurs whenever a dispute is won, lost or expired
v	issuing_dispute.created	Occurs whenever a dispute is created
v	issuing_dispute.funds_reinstated	Occurs whenever funds are reinstated to your account for an Issuing dispute
v	issuing_dispute.submitted	Occurs whenever a dispute is submitted
v	issuing_dispute.updated	Occurs whenever a dispute is updated
v	issuing_transaction.created	Occurs whenever an issuing transaction is created
v	issuing_transaction.updated	Occurs whenever an issuing transaction is updated
v	mandate.updated	Occurs whenever a Mandate is updated
v	order.created	Occurs whenever an order is created
v	order.payment_failed	Occurs whenever an order payment attempt fails
v	order.payment_succeeded	Occurs whenever an order payment attempt succeeds
v	order.updated	Occurs whenever an order is updated
v	order_return.created	Occurs whenever an order return is created
v	payment_intent.processing	Occurs when a PaymentIntent has started processing
v	payment_intent.requires_action	Occurs when a PaymentIntent transitions to requires_action state
v	payment_method.automatically_updated	Occurs whenever a payment method's details are automatically updated by the network
v	payment_method.detached	Occurs whenever a payment method is detached from a customer
v	payment_method.updated	Occurs whenever a payment method is updated via the PaymentMethod update API
v	payout.canceled	Occurs whenever a payout is canceled
v	payout.created	Occurs whenever a payout is created
v	payout.failed	Occurs whenever a payout attempt fails
v	payout.paid	Occurs whenever a payout is expected to be available in the destination account. If the payout…
v	payout.updated	Occurs whenever a payout is updated
v	person.created	Occurs whenever a person associated with an account is created
v	person.deleted	Occurs whenever a person associated with an account is deleted
v	person.updated	Occurs whenever a person associated with an account is updated
v	plan.created	Occurs whenever a plan is created
v	plan.deleted	Occurs whenever a plan is deleted
v	plan.updated	Occurs whenever a plan is updated
v	price.created	Occurs whenever a price is created
v	price.deleted	Occurs whenever a price is deleted
v	price.updated	Occurs whenever a price is updated
v	product.created	Occurs whenever a product is created
v	product.deleted	Occurs whenever a product is deleted
v	product.updated	Occurs whenever a product is updated
v	promotion_code.created	Occurs whenever a promotion code is created
v	promotion_code.updated	Occurs whenever a promotion code is updated
v	radar.early_fraud_warning.created	Occurs whenever an early fraud warning is created
v	radar.early_fraud_warning.updated	Occurs whenever an early fraud warning is updated
v	recipient.created	Occurs whenever a recipient is created
v	recipient.deleted	Occurs whenever a recipient is deleted
v	recipient.updated	Occurs whenever a recipient is updated
v	reporting.report_run.failed	Occurs whenever a requested ReportRun failed to complete
v	reporting.report_run.succeeded	Occurs whenever a requested ReportRun completed successfully
v	reporting.report_type.updated	Occurs whenever a ReportType is updated (typically to indicate that a new day's data has come…
v	review.closed	Occurs whenever a review is closed. The review's reason field indicates why: approved, disputed…
v	review.opened	Occurs whenever a review is opened
v	setup_intent.requires_action	Occurs when a SetupIntent is in requires_action state
v	sigma.scheduled_query_run.created	Occurs whenever a Sigma scheduled query run finishes
v	sku.created	Occurs whenever a SKU is created
v	sku.deleted	Occurs whenever a SKU is deleted
v	sku.updated	Occurs whenever a SKU is updated
v	source.canceled	Occurs whenever a source is canceled
v	source.chargeable	Occurs whenever a source transitions to chargeable
v	source.failed	Occurs whenever a source fails
v	source.mandate_notification	Occurs whenever a source mandate notification method is set to manual
v	source.refund_attributes_required	Occurs whenever the refund attributes are required on a receiver source to process a refund or a…
v	source.transaction.created	Occurs whenever a source transaction is created
v	source.transaction.updated	Occurs whenever a source transaction is updated
v	subscription_schedule.aborted	Occurs whenever a subscription schedule is canceled due to the underlying subscription being…
v	subscription_schedule.canceled	Occurs whenever a subscription schedule is canceled
v	subscription_schedule.completed	Occurs whenever a new subscription schedule is completed
v	subscription_schedule.created	Occurs whenever a new subscription schedule is created
v	subscription_schedule.expiring	Occurs 7 days before a subscription schedule will expire
v	subscription_schedule.released	Occurs whenever a new subscription schedule is released
v	subscription_schedule.updated	Occurs whenever a subscription schedule is updated
v	tax_rate.created	Occurs whenever a new tax rate is created
v	tax_rate.updated	Occurs whenever a tax rate is updated
v	topup.canceled	Occurs whenever a top-up is canceled
v	topup.created	Occurs whenever a top-up is created
v	topup.failed	Occurs whenever a top-up fails
v	topup.reversed	Occurs whenever a top-up is reversed
v	topup.succeeded	Occurs whenever a top-up succeeds
v	transfer.created	Occurs whenever a transfer is created
v	transfer.failed	Occurs whenever a transfer failed
v	transfer.paid	Occurs after a transfer is paid. For Instant Payouts, the event will typically be sent within 30…
v	transfer.reversed	Occurs whenever a transfer is reversed, including partial reversals
v	transfer.updated	Occurs whenever a transfer's description or metadata is updated
v	balance.available	Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid…
v	charge.captured	Occurs whenever a previously uncaptured charge is captured
v	charge.dispute.created	Occurs whenever a customer disputes a charge with their bank
v	charge.failed	Occurs whenever a failed charge attempt occurs
v	charge.refunded	Occurs whenever a charge is refunded, including partial refunds
v	charge.succeeded	Occurs whenever a new charge is created and is successful
v	checkout.session.completed	Occurs when a Checkout Session has been successfully completed
v	customer.created	Occurs whenever a new customer is created
v	customer.deleted	Occurs whenever a customer is deleted
v	customer.source.created	Occurs whenever a new source is created for a customer
v	customer.source.updated	Occurs whenever a source's details are changed
v	customer.subscription.created	Occurs whenever a customer is signed up for a new plan
v	customer.subscription.deleted	Occurs whenever a customer's subscription ends
v	customer.subscription.updated	Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the…
v	customer.updated	Occurs whenever any property of a customer changes
v	invoice.created	Occurs whenever a new invoice is created
v	invoice.finalized	Occurs whenever a draft invoice is finalized and updated to be an open invoice
v	invoice.payment_failed	Occurs whenever an invoice payment attempt fails, due either to a declined payment or to the lack…
v	invoice.payment_succeeded	Occurs whenever an invoice payment attempt succeeds
v	invoice.updated	Occurs whenever an invoice changes (e.g., the invoice amount)
v	issuing_authorization.request	Represents a synchronous request for authorization
v	issuing_card.created	Occurs whenever a card is created
v	issuing_cardholder.created	Occurs whenever a cardholder is created
v	payment_intent.amount_capturable_updated	Occurs when a PaymentIntent has funds to be captured
v	payment_intent.canceled	Occurs when a PaymentIntent is canceled
v	payment_intent.created	Occurs when a new PaymentIntent is created
v	payment_intent.payment_failed	Occurs when a PaymentIntent has failed the attempt to create a payment method or a payment
v	payment_intent.succeeded	Occurs when a PaymentIntent has successfully completed payment
v	payment_method.attached	Occurs whenever a new payment method is attached to a customer
v	setup_intent.canceled	Occurs when a SetupIntent is canceled
v	setup_intent.created	Occurs when a new SetupIntent is created
v	setup_intent.setup_failed	Occurs when a SetupIntent has failed the attempt to setup a payment method
v	setup_intent.succeeded	Occurs when an SetupIntent has successfully setup a payment method
=	listen	--color
v	on	
v	off	
v	auto	
=	listen	--config
t	filepaths
=	listen	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	trigger
o	--stripe-account	Sets a header identifying the connected account	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	trigger	--color
v	on	
v	off	
v	auto	
=	trigger	--config
t	filepaths
=	trigger	--log-level
v	info	
v	debug	
v	warn	
v	error	
#	trigger	1
v	balance.available	Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid…
v	charge.captured	Occurs whenever a previously uncaptured charge is captured
v	charge.dispute.created	Occurs whenever a customer disputes a charge with their bank
v	charge.failed	Occurs whenever a failed charge attempt occurs
v	charge.refunded	Occurs whenever a charge is refunded, including partial refunds
v	charge.succeeded	Occurs whenever a new charge is created and is successful
v	checkout.session.completed	Occurs when a Checkout Session has been successfully completed
v	customer.created	Occurs whenever a new customer is created
v	customer.deleted	Occurs whenever a customer is deleted
v	customer.source.created	Occurs whenever a new source is created for a customer
v	customer.source.updated	Occurs whenever a source's details are changed
v	customer.subscription.created	Occurs whenever a customer is signed up for a new plan
v	customer.subscription.deleted	Occurs whenever a customer's subscription ends
v	customer.subscription.updated	Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the…
v	customer.updated	Occurs whenever any property of a customer changes
v	invoice.created	Occurs whenever a new invoice is created
v	invoice.finalized	Occurs whenever a draft invoice is finalized and updated to be an open invoice
v	invoice.payment_failed	Occurs whenever an invoice payment attempt fails, due either to a declined payment or to the lack…
v	invoice.payment_succeeded	Occurs whenever an invoice payment attempt succeeds
v	invoice.updated	Occurs whenever an invoice changes (e.g., the invoice amount)
v	issuing_authorization.request	Represents a synchronous request for authorization
v	issuing_card.created	Occurs whenever a card is created
v	issuing_cardholder.created	Occurs whenever a cardholder is created
v	payment_intent.amount_capturable_updated	Occurs when a PaymentIntent has funds to be captured
v	payment_intent.canceled	Occurs when a PaymentIntent is canceled
v	payment_intent.created	Occurs when a new PaymentIntent is created
v	payment_intent.payment_failed	Occurs when a PaymentIntent has failed the attempt to create a payment method or a payment
v	payment_intent.succeeded	Occurs when a PaymentIntent has successfully completed payment
v	payment_method.attached	Occurs whenever a new payment method is attached to a customer
v	setup_intent.canceled	Occurs when a SetupIntent is canceled
v	setup_intent.created	Occurs when a new SetupIntent is created
v	setup_intent.setup_failed	Occurs when a SetupIntent has failed the attempt to setup a payment method
v	setup_intent.succeeded	Occurs when an SetupIntent has successfully setup a payment method
@	events resend
o	--account	Resend the event to the given Stripe account	v
o	--param	Key-value data to send along with the API request	v
o	-webhook-endpoint	Resends the event to the given webhook endpoint ID	v
o	-s|--show-headers	Shows response HTTP headers	
o	-c|--confirm	Skips the warning prompt and automatically confirms the command being entered	
o	--dark-style	Uses a darker color scheme	
o	-d|--data	Additional data to send with an API request	v
o	-e|--expand	Response attributes to expand inline	v
o	-i|--idempotency	Sets an idempotency key for the request, preventing the same request from replaying within 24 hours	v
o	--live	Makes a live request	
o	--stripe-account	Specify the Stripe account to use for this request	v
o	-v|--stripe-version	Specify the Stripe API version to use for this request	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	events resend	--color
v	on	
v	off	
v	auto	
=	events resend	--config
t	filepaths
=	events resend	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	get
o	-b|--ending-before	Retrieves the previous page in the list	v
o	-l|--limit	Number of objects to return	v
o	-a|--starting-after	Retrieves the next page in the list	v
o	-s|--show-headers	Shows response HTTP headers	
o	-c|--confirm	Skips the warning prompt and automatically confirms the command being entered	
o	--dark-style	Uses a darker color scheme	
o	-d|--data	Additional data to send with an API request	v
o	-e|--expand	Response attributes to expand inline	v
o	-i|--idempotency	Sets an idempotency key for the request, preventing the same request from replaying within 24 hours	v
o	--live	Makes a live request	
o	--stripe-account	Specify the Stripe account to use for this request	v
o	-v|--stripe-version	Specify the Stripe API version to use for this request	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	get	--color
v	on	
v	off	
v	auto	
=	get	--config
t	filepaths
=	get	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	post
o	-s|--show-headers	Shows response HTTP headers	
o	-c|--confirm	Skips the warning prompt and automatically confirms the command being entered	
o	--dark-style	Uses a darker color scheme	
o	-d|--data	Additional data to send with an API request	v
o	-e|--expand	Response attributes to expand inline	v
o	-i|--idempotency	Sets an idempotency key for the request, preventing the same request from replaying within 24 hours	v
o	--live	Makes a live request	
o	--stripe-account	Specify the Stripe account to use for this request	v
o	-v|--stripe-version	Specify the Stripe API version to use for this request	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	post	--color
v	on	
v	off	
v	auto	
=	post	--config
t	filepaths
=	post	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	delete
o	-s|--show-headers	Shows response HTTP headers	
o	-c|--confirm	Skips the warning prompt and automatically confirms the command being entered	
o	--dark-style	Uses a darker color scheme	
o	-d|--data	Additional data to send with an API request	v
o	-e|--expand	Response attributes to expand inline	v
o	-i|--idempotency	Sets an idempotency key for the request, preventing the same request from replaying within 24 hours	v
o	--live	Makes a live request	
o	--stripe-account	Specify the Stripe account to use for this request	v
o	-v|--stripe-version	Specify the Stripe API version to use for this request	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	delete	--color
v	on	
v	off	
v	auto	
=	delete	--config
t	filepaths
=	delete	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	samples
s	create	
s	list	Lists available Stripe Samples
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	samples	--color
v	on	
v	off	
v	auto	
=	samples	--config
t	filepaths
=	samples	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	samples create
o	--force-refresh	Force a refresh of the chaced list of Stripe Samples	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	2	0
=	samples create	--color
v	on	
v	off	
v	auto	
=	samples create	--config
t	filepaths
=	samples create	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	samples list
o	--force-refresh	Force a refresh of the chaced list of Stripe Samples	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	samples list	--color
v	on	
v	off	
v	auto	
=	samples list	--config
t	filepaths
=	samples list	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	serve
o	--port	Port the HTTP server should use	v
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
a	1	0
=	serve	--color
v	on	
v	off	
v	auto	
=	serve	--config
t	filepaths
=	serve	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	terminal quickstart
o	--api-key		v
@	logout
o	-a|--all	Removes credentials for all projects listed in your config	
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	logout	--color
v	on	
v	off	
v	auto	
=	logout	--config
t	filepaths
=	logout	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	feedback
o	--api-key	Sets your API key to use for the command	v
o	--color	Enables or disables color output	v
o	--config	Sets your config file	v
o	--device-name	Runs command on behlaf of another device	v
o	-h|--help	Provides the help documentation for commands, flags, and arguments	
o	--log-level	Set the level of detail for log messages	v
o	-v|--version	Prints the version of the Stripe CLI	
=	feedback	--color
v	on	
v	off	
v	auto	
=	feedback	--config
t	filepaths
=	feedback	--log-level
v	info	
v	debug	
v	warn	
v	error	
@	help
a	1	0
@	version
a	1	0
