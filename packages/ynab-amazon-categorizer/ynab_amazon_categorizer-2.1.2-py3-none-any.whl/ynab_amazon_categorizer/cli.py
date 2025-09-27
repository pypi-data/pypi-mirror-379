import json
import os  # For history file path
from collections.abc import Iterable
from typing import Optional, Union

# --- NEW: Import prompt_toolkit components ---
from prompt_toolkit import prompt
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent

from .amazon_parser import AmazonParser, Order

# --- END NEW ---
# --- Import extracted modules ---
from .config import Config
from .memo_generator import MemoGenerator
from .transaction_matcher import TransactionMatcher
from .ynab_client import YNABClient

# --- CONFIGURATION ---


AMAZON_PAYEE_KEYWORDS = ["amazon", "amzn", "amz"]
YNAB_API_URL = "https://api.ynab.com/v1"

# --- Amazon Order Link Functions ---


# NOTE: Memo generation functions have been moved to memo_generator.py


# NOTE: Amazon order parsing has been moved to amazon_parser.py


def prompt_for_amazon_orders_data() -> Optional[list[Order]]:
    """Prompt user to paste Amazon orders page data"""
    print("\n--- Amazon Orders Data Entry ---")
    print("You can copy and paste the content from your Amazon orders page.")
    print("This will help automatically extract order details and item information.")

    print("\nPaste Amazon orders page content:")

    orders_text = get_multiline_input_with_custom_submit("Paste here: ")

    if orders_text is None or orders_text.strip().lower() == "skip":
        print("Skipping Amazon orders data entry.")
        return None

    if not orders_text.strip():
        return None

    # Use extracted Amazon parser
    amazon_parser = AmazonParser()
    parsed_orders = amazon_parser.parse_orders_page(orders_text)

    # Show what was parsed
    if parsed_orders:
        print(f"\n✓ Successfully parsed {len(parsed_orders)} orders from Amazon data")
        for order in parsed_orders[:3]:
            print(f"  - Order {order.order_id}: ${order.total} on {order.date_str}")
        if len(parsed_orders) > 3:
            print(f"  ... and {len(parsed_orders) - 3} more orders")
    else:
        print("\nNo orders could be parsed from the provided text.")
        print("This might be due to formatting differences in the copied text.")

    return parsed_orders


# NOTE: find_matching_order moved to transaction_matcher.py


def get_multiline_input_with_custom_submit(
    prompt_message: str = "Enter multiline text: ",
) -> Optional[str]:
    """Get multiline input with Ctrl+J to submit"""
    kb = KeyBindings()

    @kb.add("escape", "enter")  # Binds Alt+Enter to submit
    def _(event: KeyPressEvent) -> None:
        """When Alt+Enter is pressed, accept the current buffer's text."""
        event.app.exit(result=event.app.current_buffer.text)

    print("Press Enter for a new line.")
    print("Submit by pressing Alt+Enter.")
    print("Press Ctrl+C to cancel.")

    try:
        user_input = prompt(prompt_message, multiline=True, key_bindings=kb)
        return user_input
    except EOFError:
        print("\nInput cancelled (EOF).")
        return None
    except KeyboardInterrupt:
        print("\nInput cancelled (KeyboardInterrupt).")
        return None


def generate_split_summary_memo(matching_order: Order) -> str:
    """Generate a summary memo for split transactions showing all items"""
    if (
        not matching_order
        or not hasattr(matching_order, "items")
        or not matching_order.items
    ):
        return ""

    items = matching_order.items
    if len(items) == 1:
        return items[0]

    # Format as: "2 Items:\n- Item 1\n- Item 2"
    summary = f"{len(items)} Items:"
    for item in items:
        summary += f"\n- {item}"

    return summary


def prompt_for_item_details() -> Optional[
    dict[str, Union[str, int, float, list[str], None]]
]:
    """Prompt user to enter item details manually"""
    print("\n--- Manual Item Details Entry ---")

    item_details: dict[str, Union[str, int, float, list[str], None]] = {}

    # Get item title/description
    title = input("Enter item title/description (optional): ").strip()
    if title:
        item_details["title"] = title

    # Get quantity
    while True:
        qty_input = input("Enter quantity (optional, press Enter to skip): ").strip()
        if not qty_input:
            break
        try:
            quantity = int(qty_input)
            if quantity > 0:
                item_details["quantity"] = quantity
                break
            else:
                print("Quantity must be positive.")
        except ValueError:
            print("Please enter a valid number.")

    # Get price per item
    while True:
        price_input = input(
            "Enter item price (optional, press Enter to skip): "
        ).strip()
        if not price_input:
            break
        try:
            price = float(price_input.replace("$", "").replace(",", ""))
            if price >= 0:
                item_details["price"] = price
                break
            else:
                print("Price must be non-negative.")
        except ValueError:
            print("Please enter a valid price (e.g., 29.99).")

    return item_details if item_details else None


# --- Helper Functions ---
# NOTE: YNAB API functions have been moved to ynab_client.py


# NOTE: update_ynab_transaction moved to ynab_client.py


# NOTE: get_categories moved to ynab_client.py


class CategoryCompleter(Completer):
    # ... (implementation from v3) ...
    def __init__(self, category_list: list[tuple[str, str]]) -> None:
        self.categories = [name for name, _id in category_list]
        self.category_list = category_list

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text_before_cursor = document.text_before_cursor.lower()
        if text_before_cursor:
            for category_name in self.categories:
                if text_before_cursor in category_name.lower():
                    yield Completion(
                        category_name, start_position=-len(text_before_cursor)
                    )


def prompt_for_category_selection(
    category_completer: CategoryCompleter, name_to_id_map: dict[str, str]
) -> tuple[Optional[str], Optional[str]]:
    # ... (implementation from v3) ...
    history_file = os.path.join(os.path.expanduser("~"), ".ynab_amazon_cat_history")
    history = FileHistory(history_file)
    while True:
        try:
            user_input = prompt(
                "Enter category name (Tab to complete, Enter to confirm, leave empty or type 'b' to go back): ",
                completer=category_completer,
                history=history,
                reserve_space_for_menu=5,
            ).strip()
            if not user_input or user_input.lower() == "b":
                return None, None
            input_lower = user_input.lower()
            if input_lower in name_to_id_map:
                selected_id = name_to_id_map[input_lower]
                selected_display_name = ""
                for name, cat_id in category_completer.category_list:
                    if cat_id == selected_id:
                        selected_display_name = name
                        break
                print(f"Selected: {selected_display_name}")
                return selected_id, selected_display_name
            else:
                print(
                    f"Error: '{user_input}' is not a recognized category. Please use Tab completion or try again."
                )
        except EOFError:
            print("\nOperation cancelled by user (EOF).")
            return None, None
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (KeyboardInterrupt).")
            return None, None


# --- Main Script Logic ---


def main() -> None:
    """Main CLI function."""
    # Load configuration using extracted Config class
    try:
        config = Config.from_env()
        print("✓ Configuration loaded successfully")
        print(f"✓ API Key: {config.api_key[:8]}...")
        print(f"✓ Budget ID: {config.budget_id[:8]}...")
        print(
            f"✓ Account ID: {config.account_id[:8]}..."
            if config.account_id
            else "✓ All accounts"
        )
    except Exception as e:
        print(f"ERROR: {e}")
        print("Please set environment variables or create a .env file.")
        print("See README.md for setup instructions.")
        exit(1)

    # Initialize YNAB client
    ynab_client = YNABClient(config.api_key, config.budget_id)

    print("Fetching categories...")
    categories_list, category_name_map, category_id_map = ynab_client.get_categories()

    if not categories_list:
        print("Exiting due to category fetch error or no usable categories found.")
        exit()

    category_completer_instance = CategoryCompleter(categories_list)
    print(f"\nFound {len(categories_list)} usable categories. Completion enabled.")

    # Setup history for memo input (optional, but can be nice)
    os.path.join(os.path.expanduser("~"), ".ynab_amazon_memo_history")

    # Ask user if they want to provide Amazon orders data for automatic item detection
    print("\n--- Optional: Amazon Orders Data ---")
    print(
        "You can paste Amazon orders page content to automatically match transactions with order details."
    )
    provide_orders = input(
        "Would you like to provide Amazon orders data? (y/n, default y): "
    ).lower()
    if not provide_orders:
        provide_orders = "y"

    parsed_orders = None
    if provide_orders == "y":
        parsed_orders = prompt_for_amazon_orders_data()
        if parsed_orders:
            print(f"✓ Parsed {len(parsed_orders)} orders from Amazon data")
            for order in parsed_orders[:3]:  # Show first 3
                print(
                    f"  - Order {order.order_id}: ${getattr(order, 'total', 'N/A')} ({len(getattr(order, 'items', []))} items)"
                )
            if len(parsed_orders) > 3:
                print(f"  ... and {len(parsed_orders) - 3} more orders")
        else:
            print("No valid orders found in provided data.")

    print("\nFetching transactions...")
    # (Transaction fetching and filtering logic remains the same as v3)
    transactions_endpoint = f"/budgets/{config.budget_id}/transactions"
    if config.account_id and config.account_id.lower() != "none":
        transactions_endpoint = (
            f"/budgets/{config.budget_id}/accounts/{config.account_id}/transactions"
        )
    transactions_data = ynab_client.get_data(transactions_endpoint)
    if transactions_data is None or "transactions" not in transactions_data:
        exit()
    transactions = transactions_data["transactions"]
    print(f"Fetched {len(transactions)} transactions.")
    transactions_to_process = []
    for t in transactions:
        # ... (Filtering logic same as v3) ...
        payee_name = t.get("payee_name", "").lower() if t.get("payee_name") else ""
        is_amazon = any(keyword in payee_name for keyword in AMAZON_PAYEE_KEYWORDS)
        is_uncategorized = t.get("category_id") is None
        is_not_reconciled = t.get("cleared") != "reconciled"
        is_valid_for_processing = (
            is_amazon
            and is_uncategorized
            and is_not_reconciled
            and t.get("amount", 0) != 0
            and t.get("transfer_account_id") is None
            and not t.get("subtransactions")
            and t.get("import_id") is not None
        )
        if is_valid_for_processing:
            transactions_to_process.append(t)
    print(
        f"\nFound {len(transactions_to_process)} uncategorized Amazon transaction(s) needing attention."
    )

    # --- Process Transactions (Main Loop) ---
    for i, t in enumerate(transactions_to_process):
        # ... (transaction detail extraction same as v3) ...
        transaction_id = t["id"]
        date = t["date"]
        payee = t.get("payee_name", "N/A")
        amount_milliunits = t["amount"]
        amount_float = amount_milliunits / 1000.0
        original_memo = t.get("memo", "")

        if amount_milliunits > 0:
            print(f"Found inflow transaction: {payee} ${amount_float:.2f}")
            process_inflow = input(
                "Process this inflow (refund/credit)? (y/n, default n): "
            ).lower()
            if process_inflow != "y":
                print("Skipping inflow transaction.")
                continue

        print(
            f"\n--- Processing Transaction {i + 1}/{len(transactions_to_process)} ---"
        )
        print(f"  ID:   {transaction_id}")
        print(f"  Date: {date}")
        print(f"  Payee: {payee}")
        print(f"  Amount: {-amount_float:.2f}")
        if original_memo:
            print(f"  Original Memo: {original_memo}")

        # Try to find matching order from parsed data and show it
        matching_order = None
        if parsed_orders:
            # Use extracted transaction matcher
            transaction_matcher = TransactionMatcher()
            matching_order = transaction_matcher.find_matching_order(
                amount_float, date, parsed_orders
            )
            if matching_order:
                print("\n  🎯 MATCHED ORDER FOUND:")
                if isinstance(matching_order, Order):
                    order_id = matching_order.order_id
                    total = matching_order.total
                    date_str = matching_order.date_str
                    items = matching_order.items
                else:
                    order_id = matching_order.get("order_id")
                    total = matching_order.get("total")
                    date_str = matching_order.get("date") or matching_order.get(
                        "date_str"
                    )
                    items = matching_order.get("items", [])

                print(f"     Order ID: {order_id}")
                print(f"     Total: ${total if total is not None else 'N/A'}")
                print(f"     Date: {date_str if date_str is not None else 'N/A'}")
                # Use extracted memo generator for order link
                memo_generator = MemoGenerator()
                order_link = memo_generator.generate_amazon_order_link(order_id)
                print(f"     Order Link: {order_link}")
                if items:
                    print("     Items:")
                    for item in items:
                        print(f"       - {item}")
                print()
            else:
                print("  ⚠ No matching order found in parsed Amazon data")

        while True:  # Action loop (c, s, q)
            action = input(
                "Action? (c = categorize/split, s = skip, q = quit, default c): "
            ).lower()
            if not action:
                action = "c"
            if action == "q":
                print("Quitting.")
                exit()
            elif action == "s":
                print("Skipping.")
                break  # Next transaction
            elif action == "c":
                # --- Categorization Logic ---
                updated_payload_dict = None

                # Check if there are multiple items and suggest splitting
                # Check if we should offer splitting
                should_offer_split = False
                if matching_order:
                    if isinstance(matching_order, Order):
                        should_offer_split = bool(
                            matching_order.items and len(matching_order.items) > 1
                        )
                    else:
                        items = matching_order.get("items", [])
                        should_offer_split = bool(items and len(items) > 1)

                if should_offer_split:
                    print("There is more than one item in this transaction.")

                split_decision = input(
                    "Split this transaction? (y/n, default n): "
                ).lower()

                if split_decision != "y":
                    # --- SINGLE CATEGORY ---
                    print("Enter category name for the transaction:")
                    category_id, category_name = prompt_for_category_selection(
                        category_completer_instance, category_name_map
                    )
                    if category_id is None:
                        continue  # Back to action prompt

                    # --- ENHANCED MEMO INPUT WITH AUTOMATIC ITEM DETECTION ---
                    item_details: Optional[
                        dict[str, Union[str, int, float, list[str], None]]
                    ] = None
                    enhanced_memo = None

                    # Use matched order data or prompt for manual entry
                    if matching_order:
                        print("Using matched order data for memo generation...")
                        if isinstance(matching_order, Order):
                            item_details = {
                                "order_id": matching_order.order_id or "",
                                "items": matching_order.items,
                                "total": matching_order.total,
                                "date": matching_order.date_str,
                            }
                        else:
                            item_details = {
                                "order_id": matching_order.get("order_id", ""),
                                "items": matching_order.get("items", []),
                                "total": matching_order.get("total"),
                                "date": matching_order.get("date")
                                or matching_order.get("date_str"),
                            }
                    else:
                        # Ask if user wants to enter item details manually
                        manual_entry = input(
                            "No order match found. Enter item details manually? (y/n, default n): "
                        ).lower()
                        if manual_entry == "y":
                            item_details = prompt_for_item_details()
                        else:
                            item_details = None

                    if item_details:
                        if isinstance(item_details, dict) and "items" in item_details:
                            # Auto-matched order data - format as: Item Name\n Order Link
                            items_list = item_details["items"]
                            items_text = (
                                items_list[0]
                                if isinstance(items_list, list) and items_list
                                else "Amazon Purchase"
                            )
                            # Use extracted memo generator
                            memo_generator = MemoGenerator()
                            order_id_value = item_details["order_id"]
                            order_link = memo_generator.generate_amazon_order_link(
                                order_id_value
                                if isinstance(order_id_value, str)
                                else None
                            )
                            enhanced_memo = (
                                f"{items_text}\n {order_link}"
                                if order_link
                                else items_text
                            )
                        else:
                            # Manual item details - use extracted memo generator
                            memo_generator = MemoGenerator()
                            enhanced_memo = memo_generator.generate_enhanced_memo(
                                original_memo, None, item_details
                            )
                    else:
                        # No item details
                        enhanced_memo = original_memo

                    if enhanced_memo and enhanced_memo != original_memo:
                        print("\nSuggested memo:")
                        print(f"'{enhanced_memo}'")
                        use_suggested = input(
                            "Use suggested memo? (y/n, default y): "
                        ).lower()
                        if use_suggested != "n":
                            memo_input = enhanced_memo
                        else:
                            print("Enter custom memo (multiline):")
                            memo_input = get_multiline_input_with_custom_submit("> ")
                            if memo_input is None:
                                memo_input = ""
                            else:
                                memo_input = memo_input.strip()
                    else:
                        print("Enter optional memo (multiline):")
                        memo_input = get_multiline_input_with_custom_submit("> ")
                        if memo_input is None:
                            memo_input = ""
                        else:
                            memo_input = memo_input.strip()
                    # --- END ENHANCED MEMO INPUT ---

                    update_payload = {
                        # ... (id, account_id, date, amount etc. same as v3) ...
                        "id": transaction_id,
                        "account_id": t["account_id"],
                        "date": t["date"],
                        "amount": amount_milliunits,
                        "payee_id": t.get("payee_id"),
                        "payee_name": payee,
                        "category_id": category_id,
                        "memo": memo_input
                        if memo_input
                        else original_memo,  # Use new memo or keep original
                        "cleared": t.get("cleared"),
                        "approved": True,
                        "flag_color": t.get("flag_color"),
                        "import_id": t.get("import_id"),
                    }
                    updated_payload_dict = update_payload

                else:
                    # --- SPLITTING ---
                    print("\n--- Splitting Transaction ---")
                    subtransactions: list[dict[str, Union[int, str, None]]] = []
                    remaining_milliunits = amount_milliunits
                    split_count = 1

                    while remaining_milliunits != 0:
                        print(
                            f"\nSplit {split_count}: Amount remaining: {abs(remaining_milliunits / 1000.0):.2f}"
                        )

                        # Show which item this split is for if we have matched order data
                        # Show which item this split is for if we have matched order data
                        items = []
                        if matching_order:
                            if isinstance(matching_order, Order):
                                items = matching_order.items or []
                            else:
                                items = matching_order.get("items", [])

                        if items:
                            if split_count <= len(items):
                                print(f"Item {split_count}: {items[split_count - 1]}")
                            else:
                                print("Additional split for remaining items")

                        print(f"Enter category name for split {split_count}:")
                        category_id, category_name = prompt_for_category_selection(
                            category_completer_instance, category_name_map
                        )
                        if category_id is None:  # User backed out
                            print("Cancelling split process.")
                            subtransactions = []  # Clear partial splits
                            break  # Back to action prompt

                        # Get amount for this split (logic same as v3)
                        while True:
                            try:
                                max_amount = abs(remaining_milliunits / 1000.0)
                                amount_str = input(
                                    f"Enter amount for '{category_name}' (positive, max {max_amount:.2f}, default {max_amount:.2f}): "
                                )
                                if not amount_str:
                                    amount_str = str(max_amount)
                                # ... (amount validation and calculation same as v3) ...
                                split_amount_float = float(amount_str)
                                if split_amount_float <= 0:
                                    print("Amount must be positive.")
                                    continue
                                split_amount_milliunits = int(
                                    round(split_amount_float * 1000)
                                )
                                if (
                                    split_amount_milliunits
                                    > abs(remaining_milliunits) + 1
                                ):
                                    print(
                                        f"Amount exceeds remaining. Max {abs(remaining_milliunits / 1000.0):.2f}"
                                    )
                                    continue
                                split_amount_milliunits = -abs(
                                    split_amount_milliunits
                                )  # Ensure negative for outflow
                                if (
                                    abs(split_amount_milliunits - remaining_milliunits)
                                    <= 1
                                ):  # Equal or very close
                                    print("Amount covers remaining balance.")
                                    split_amount_milliunits = (
                                        remaining_milliunits  # Assign exact remainder
                                    )
                                elif split_amount_milliunits > abs(
                                    remaining_milliunits
                                ):
                                    continue  # Should be caught, but safety
                                break  # Amount valid
                            except ValueError:
                                print("Invalid amount.")

                        # --- ENHANCED SPLIT MEMO INPUT ---
                        # Generate memo for each split based on matched order data
                        split_memo: Optional[str] = None
                        suggested_split_memo: str = ""

                        # Use the already matched order if available
                        if matching_order:
                            print("Using matched order data for split memo...")
                            if isinstance(matching_order, Order):
                                items = matching_order.items
                                order_id = matching_order.order_id
                            else:
                                items = matching_order.get("items", [])
                                order_id = matching_order.get("order_id")

                            if split_count <= len(items):
                                # Use the specific item for this split
                                items_text = items[split_count - 1]
                                # Use extracted memo generator
                                memo_generator = MemoGenerator()
                                order_link = memo_generator.generate_amazon_order_link(
                                    order_id
                                )
                                suggested_split_memo = (
                                    f"{items_text}\n {order_link}"
                                    if order_link
                                    else items_text
                                )
                            else:
                                # Fallback for extra splits beyond available items
                                suggested_split_memo = "Additional item"
                        else:
                            # Ask if user wants to enter item details manually for split
                            manual_entry = input(
                                "Enter item details for this split? (y/n, default n): "
                            ).lower()
                            if manual_entry == "y":
                                item_details = prompt_for_item_details()
                                if item_details:
                                    # Use extracted memo generator
                                    memo_generator = MemoGenerator()
                                    suggested_split_memo = (
                                        memo_generator.generate_enhanced_memo(
                                            "", None, item_details
                                        )
                                    )

                        # Present the memo suggestion
                        if suggested_split_memo:
                            print(f"Suggested memo for '{category_name}' split:")
                            print(f"'{suggested_split_memo}'")
                            use_suggested = input(
                                "Use suggested memo? (y/n, default y): "
                            ).lower()
                            if use_suggested != "n":
                                split_memo = suggested_split_memo
                            else:
                                print(
                                    f"Enter custom memo for '{category_name}' split (multiline):"
                                )
                                split_memo = get_multiline_input_with_custom_submit(
                                    "> "
                                )
                                if split_memo is None:
                                    split_memo = ""
                                else:
                                    split_memo = split_memo.strip()
                        else:
                            print(
                                f"Enter optional memo for '{category_name}' split (multiline):"
                            )
                            split_memo_input = get_multiline_input_with_custom_submit(
                                "> "
                            )
                            split_memo = (
                                split_memo_input.strip()
                                if split_memo_input is not None
                                else ""
                            )
                        # --- END ENHANCED SPLIT MEMO INPUT ---

                        subtransactions.append(
                            {
                                "amount": split_amount_milliunits,
                                "category_id": category_id,
                                "memo": split_memo if split_memo else None,
                            }
                        )

                        remaining_milliunits -= split_amount_milliunits
                        split_count += 1

                        if abs(remaining_milliunits) <= 1:  # Handle tiny remainder
                            print("Remaining amount negligible.")
                            if subtransactions:
                                print(
                                    f"Adjusting last split amount by {remaining_milliunits} milliunits."
                                )
                                subtransactions[-1]["amount"] += remaining_milliunits
                            remaining_milliunits = 0  # Force complete

                    # End of splitting loop
                    if remaining_milliunits == 0 and subtransactions:
                        update_payload = {
                            # ... (id, account_id, date, amount etc. same as v3) ...
                            "id": transaction_id,
                            "account_id": t["account_id"],
                            "date": t["date"],
                            "amount": amount_milliunits,
                            "payee_id": t.get("payee_id"),
                            "payee_name": payee,
                            "category_id": None,  # Null for splits
                            "memo": generate_split_summary_memo(matching_order)
                            if matching_order and isinstance(matching_order, Order)
                            else original_memo,  # Generate summary memo for splits
                            "cleared": t.get("cleared"),
                            "approved": True,
                            "flag_color": t.get("flag_color"),
                            "import_id": t.get("import_id"),
                            "subtransactions": subtransactions,
                        }
                        updated_payload_dict = update_payload
                    else:
                        print("Splitting cancelled. No changes will be made.")
                        # updated_payload_dict remains None

                # --- Confirmation and API Call (same as v3) ---
                if updated_payload_dict:
                    print("\n--- Preview Update ---")
                    # Add category names to preview for better readability
                    preview_dict = updated_payload_dict.copy()
                    if preview_dict.get("category_id"):
                        category_name = category_id_map.get(
                            preview_dict["category_id"], "Unknown Category"
                        )
                        preview_dict["category_name"] = category_name
                    if preview_dict.get("subtransactions"):
                        for subtrans in preview_dict["subtransactions"]:
                            if subtrans.get("category_id"):
                                cat_name = category_id_map.get(
                                    subtrans["category_id"], "Unknown Category"
                                )
                                subtrans["category_name"] = cat_name
                    print(json.dumps(preview_dict, indent=2, ensure_ascii=False))
                    confirm = input("Confirm update? (y/n, default y): ").lower()
                    if not confirm:
                        confirm = "y"
                    if confirm == "y":
                        if ynab_client.update_transaction(
                            transaction_id, updated_payload_dict
                        ):
                            print("Update successful.")
                            break  # Exit action loop, go to next transaction
                        else:
                            print("Update failed.")
                            continue  # Back to action prompt
                    else:
                        print("Update cancelled.")
                        continue  # Back to action prompt
                elif action == "c":
                    continue  # Back to action prompt if categorization started but didn't complete
                else:
                    continue  # Back to action prompt

            else:  # Invalid action
                print("Invalid action. Choose 'c', 's', or 'q'.")
                # Loop continues asking for action

    # End of processing loop
    print("\nFinished processing transactions.")


if __name__ == "__main__":
    main()
