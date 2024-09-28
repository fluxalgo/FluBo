from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import logging
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start function to display the main menu
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🤖 Subscriptions", callback_data='subscriptions')],
        [InlineKeyboardButton("📖 More about Flux Algo", callback_data='more_about')],
        [InlineKeyboardButton("🌍 Public Channel", url="https://t.me/fluxalgo")],
        [InlineKeyboardButton("🔐 Flux Algo Exclusive Channel", url="https://t.me/+w8g56UExratmYzNk")],  # New button added
        [InlineKeyboardButton("🧑‍💻 Support", url="https://t.me/fluxalgo_support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        await update.callback_query.message.edit_text('Hello! Welcome to Flux Algo bot menu:', reply_markup=reply_markup)
    else:
        await update.message.reply_text('Hello! Welcome to Flux Algo bot menu:', reply_markup=reply_markup)

# Callback function for button presses
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'subscriptions':
        # Subscription options
        message_text = """
        Subscription Plans:
        """

        keyboard = [
            [InlineKeyboardButton("49$ - Monthly (save 51$)", callback_data='1_month')],
            [InlineKeyboardButton("144$ - 3 Months (save 156$)", callback_data='3_months')],
            [InlineKeyboardButton("279$ - 6 Months (save 321$)", callback_data='6_months')],
            [InlineKeyboardButton("549$ - 12 Months (save 651$)", callback_data='12_months')],
            [InlineKeyboardButton("999$ - Lifetime (save 1001$)", callback_data='lifetime')],
            [InlineKeyboardButton("⬅️ Back", callback_data='main_menu')]  # Back button goes to the main menu
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=message_text, reply_markup=reply_markup)

    elif query.data in ['1_month', '3_months', '6_months', '12_months', 'lifetime']:
        message_text = """
        Please click the Proceed to payment button below to complete payment.

Once we receive payment you will be notified.
        """

        keyboard = [
            [InlineKeyboardButton("Proceed to Payment", callback_data='proceed_to_payment')],
            [InlineKeyboardButton("⬅️ Back", callback_data='subscriptions')]  # Back button goes to subscriptions menu
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=message_text, reply_markup=reply_markup)

    elif query.data == 'proceed_to_payment':
        payment_details = """
        USDT Payment Info 

        Network: 
      Tron (TRC20)

        Deposit Address: TAm6F76Fxz4xVxWAqsifigXDH1pN49Uv8y

Please click the Payment Complete button below to send payment confirmation.

Once confirmed you will be notified.
        """

        keyboard = [
            [InlineKeyboardButton("Payment Complete", url="https://t.me/fluxalgo_support")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=payment_details, reply_markup=reply_markup)

    elif query.data == 'more_about':
        message_text = """
        Please select a topic:
        """
        keyboard = [
            [InlineKeyboardButton("📝 How it works?", callback_data='how_it_works')],
            [InlineKeyboardButton("🎯 What’s the Accuracy?", callback_data='accuracy')],
            [InlineKeyboardButton("🔎 Do you offer free Trial / Demo?", callback_data='free_trial')],
            [InlineKeyboardButton("🔢 How many Signals per Day?", callback_data='signals_per_day')],
            [InlineKeyboardButton("🧑‍🦯 How to use it?", callback_data='how_to_use')],
            [InlineKeyboardButton("✈️ Advantage of Flux Algo?", callback_data='advantages')],
            [InlineKeyboardButton("🚨 Are there any Alerts?", callback_data='alerts')],
            [InlineKeyboardButton("🤖 Subscriptions", callback_data='subscriptions')],
            [InlineKeyboardButton("⬅️ Back", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=message_text, reply_markup=reply_markup)

    elif query.data == 'how_it_works':
        message_text = """
        It works on TradingView. FLUX ALGO is a specially designed trading system, with powerful custom strategies for crypto.

Signals are generated directly on your TradingView chart. 
The indicator gives an Entry, Take Profit, Stoploss, DCA LEVEL, and Risk management/Position size for each signal.

You will also receive notifications of all new signals via Telegram!
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'accuracy':
        message_text = """
        The accuracy of the indicator is in the range of 80% and above, with proper risk-reward. 
This means that at least 8 out of 10 signals will be successful.
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'free_trial':
        message_text = """
        We do have a 7-day trial period. And we publish free trades in the public channel here — https://t.me/fluxalgo for free to demonstrate its performance.

You can also see reviews about us on our main channel using the #review tag. 
You can also see our performances and video reports on the main channel.
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'signals_per_day':
        message_text = """
        The indicator provides 5-20 signals per day, depending on the market conditions.
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'how_to_use':
        message_text = """
        FLUX ALGO is very easy to use; we made sure it’s user-friendly.

Flux Algo generates signals directly on your chart, also sends the signals to the telegram alert channel. 
You just have to open the position on the exchange you use and set take profits and stop loss accordingly and wait for profit! 💰

You will receive signals in a user-friendly format.  
Each signal contains take profits, stop loss, entry points, and DCA (dollar cost averaging) level.

A free TradingView account is enough to use Flux Algo.
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'advantages':
        message_text = """
        Flux Algo is a Trading Algorithm developed using our technical analysis system to forecast the market movement and alert you.

The core value and goal of our team is to unlock and simplify trading experience for traders from all levels, allowing them to be stress-free during their entire trading journey.

We understand how overwhelming trying to follow other indicators can be, hell, even their documentation, and trying to find the perfect configuration only for it to repaint or stop working after a few trades.

Forget about the “it works with all markets” trash indicators; Flux Algo has a set of custom powerful strategies for specific assets built by experienced traders at your fingertips, and we don’t sacrifice risk-reward for high winrate.

More? 
 — Flux Algo does not make emotional decisions that lead to huge losses.
 — Flux Algo strictly follows the algorithm and does not deviate from it.
 — Flux Algo is disciplined and always maintains composure.
 — Flux Algo does as much as possible to protect you from flat, unexpected market movements and false breakouts. 
 — You get to see the most detailed statistics for all supported tickers.
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'alerts':
        message_text = """
        Sure. It will send alerts when entering or exiting a position.

You will be notified of each new signal via Telegram!
You will receive in the notification the entry point, take profits, stop loss, and DCA levels.

Notifications will come directly to your Telegram in the most convenient format. 
Check out an example 👉 t.me/fluxalgo/2143
        """
        await send_back_subscription(query, message_text)

    elif query.data == 'main_menu':
        await start(update, context)

async def send_back_subscription(query, message_text):
    keyboard = [
        [InlineKeyboardButton("🤖 Subscriptions", callback_data='subscriptions')],
        [InlineKeyboardButton("⬅️ Back", callback_data='more_about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=message_text, reply_markup=reply_markup)

# Main function to set up handlers and run the bot
async def main():
    # Initialize the Application object with your bot token
    application = Application.builder().token("7348362971:AAFYrzxeg-JH6jyFQx3ER44PPaMqjaVhn4o").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback)) 

    # Start polling for updates
    await application.run_polling()  # Start the polling

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) == "Cannot close a running event loop":
            # Handle the case where the event loop is already running
            import nest_asyncio
            nest_asyncio.apply()
            asyncio.run(main())