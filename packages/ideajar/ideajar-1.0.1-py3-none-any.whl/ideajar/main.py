import argparse
import os
import glob
from datetime import datetime
from pathlib import Path

# Define idea storage directory and file structure
IDEA_DIR = Path.home() / '.ideajar'
CURRENT_MONTH_FILE = IDEA_DIR / f'{datetime.now().strftime("%Y-%m")}.txt'
ALL_IDEAS_FILE = IDEA_DIR / 'all_ideas.txt'  # Maintain compatibility with old version
LEGACY_FILE = Path.home() / '.ideas.txt'  # Old version file

def migrate_legacy_file():
    """Migrate old version ~/.ideas.txt file to new directory structure"""
    if LEGACY_FILE.exists() and not IDEA_DIR.exists():
        print("🔄 Detected legacy data, migrating to new storage structure...")
        setup_directory()
        
        # Read old file content
        with open(LEGACY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Write to new all_ideas.txt file
        with open(ALL_IDEAS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Backup and delete old file
        backup_file = LEGACY_FILE.with_suffix('.txt.backup')
        LEGACY_FILE.rename(backup_file)
        print(f"✅ Data migrated to {IDEA_DIR}")
        print(f"📁 Old file backed up as {backup_file}")

def setup_directory():
    """Initialize idea storage directory"""
    IDEA_DIR.mkdir(exist_ok=True)
    
    if not ALL_IDEAS_FILE.exists():
        with open(ALL_IDEAS_FILE, 'w', encoding='utf-8') as f:
            f.write("--- Your Idea Jar (Overview) ---\n")
            f.write("💡 Every great idea starts with a simple thought\n\n")

def setup():
    """Check and setup idea storage structure"""
    # First check if legacy data migration is needed
    migrate_legacy_file()
    
    # Ensure directory exists
    if not IDEA_DIR.exists():
        print("🎉 Welcome to 'ideajar'! Creating idea storage directory for you...")
        setup_directory()
        print(f"✅ Directory created at: {IDEA_DIR}")
        print("💡 Now you can start recording your ideas!")
        print("📅 Ideas will be organized by month, keeping everything tidy!")

def get_current_month_file():
    """Get current month's idea file, create if not exists"""
    if not CURRENT_MONTH_FILE.exists():
        month_name = datetime.now().strftime("%Y-%m")
        with open(CURRENT_MONTH_FILE, 'w', encoding='utf-8') as f:
            f.write(f"--- Ideas for {month_name} ---\n")
            f.write("💡 This month's inspiration records\n\n")
    return CURRENT_MONTH_FILE

def add_idea(idea_text: str):
    """Add a new idea to current month file and overview file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line_to_add = f"[{timestamp}] {idea_text}\n"
    
    # Add to current month file
    current_file = get_current_month_file()
    with open(current_file, 'a', encoding='utf-8') as f:
        f.write(line_to_add)
    
    # Also add to overview file (maintain compatibility)
    with open(ALL_IDEAS_FILE, 'a', encoding='utf-8') as f:
        f.write(line_to_add)
    
    month_name = datetime.now().strftime("%Y-%m")
    print(f"💡 Idea saved to {month_name}: \"{idea_text}\"")

def list_ideas(show_recent=True, show_all=False, month=None):
    """Display idea list"""
    if not IDEA_DIR.exists():
        print("📝 No idea directory yet. Please record an idea to get started!")
        print("💡 Usage: idea \"your idea\"")
        return
    
    if month:
        # Show ideas for specific month
        month_file = IDEA_DIR / f'{month}.txt'
        if not month_file.exists():
            print(f"📝 No ideas recorded for {month}.")
            return
        
        print(f"🎯 Ideas for {month}:")
        print("=" * 50)
        with open(month_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                print(content)
            else:
                print("📝 No ideas recorded for this month.")
        print("=" * 50)
        
    elif show_all:
        # Show all ideas
        print("🎯 All your ideas:")
        print("=" * 60)
        with open(ALL_IDEAS_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                print(content)
            else:
                print("📝 Idea jar is empty, start recording your first idea!")
        print("=" * 60)
        
    else:
        # Show current month ideas (default behavior)
        current_file = get_current_month_file()
        month_name = datetime.now().strftime("%Y-%m")
        print(f"🎯 Ideas for {month_name}:")
        print("=" * 50)
        with open(current_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            lines = content.split('\n')
            idea_lines = [line for line in lines if line.strip().startswith('[')]
            if idea_lines:
                print(content)
                if len(idea_lines) >= 5:
                    print(f"\n💡 Tip: Use 'idea --all' to view all historical ideas")
            else:
                print("📝 No ideas recorded for this month yet, start with your first idea!")
        print("=" * 50)

def list_months():
    """List all months with idea records"""
    if not IDEA_DIR.exists():
        print("📝 No idea directory yet.")
        return
    
    # Find all month files
    month_files = list(IDEA_DIR.glob('????-??.txt'))
    if not month_files:
        print("📝 No monthly idea records yet.")
        return
    
    print("📅 Idea record months:")
    print("=" * 30)
    for month_file in sorted(month_files):
        month = month_file.stem
        # Count ideas in this month
        with open(month_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        idea_count = sum(1 for line in lines if line.strip().startswith('['))
        
        print(f"📝 {month}: {idea_count} ideas")
    print("=" * 30)
    print("💡 Use 'idea --month 2024-09' to view specific month ideas")

def search_ideas(keyword):
    """Search for keyword in all ideas"""
    if not IDEA_DIR.exists():
        print("📝 No idea directory yet.")
        return
    
    print(f"🔍 Searching for keyword: \"{keyword}\"")
    print("=" * 50)
    
    found_count = 0
    
    # Search all month files
    month_files = list(IDEA_DIR.glob('????-??.txt'))
    for month_file in sorted(month_files, reverse=True):
        month = month_file.stem
        
        with open(month_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        month_found = False
        for line in lines:
            if line.strip().startswith('[') and keyword.lower() in line.lower():
                if not month_found:
                    print(f"\n📅 {month}:")
                    month_found = True
                print(f"  {line.strip()}")
                found_count += 1
    
    if found_count == 0:
        print("❌ No ideas found containing that keyword.")
    else:
        print(f"\n✅ Found {found_count} related ideas.")
    print("=" * 50)

def clear_ideas():
    """Clear all ideas with multiple confirmation steps to prevent accidental deletion"""
    if not IDEA_DIR.exists():
        print("📝 No idea directory exists, nothing to clear.")
        return
    
    # Count current ideas for display
    total_count = 0
    month_files = list(IDEA_DIR.glob('????-??.txt'))
    
    if not month_files:
        print("📝 No ideas found to clear.")
        return
    
    for month_file in month_files:
        with open(month_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        idea_count = sum(1 for line in lines if line.strip().startswith('['))
        total_count += idea_count
    
    print("🚨 " + "="*60)
    print("🚨  DANGER: PERMANENT DELETION WARNING")
    print("🚨 " + "="*60)
    print(f"📊 You currently have {total_count} ideas across {len(month_files)} months:")
    
    for month_file in sorted(month_files):
        month = month_file.stem
        with open(month_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        idea_count = sum(1 for line in lines if line.strip().startswith('['))
        print(f"   📅 {month}: {idea_count} ideas")
    
    print("\n⚠️  This operation will:")
    print("   • DELETE ALL idea records permanently")
    print("   • REMOVE ALL monthly files")
    print("   • CLEAR ALL historical data")
    print("   • This action CANNOT be undone!")
    
    print("\n" + "="*60)
    
    # First confirmation
    print("🔒 STEP 1/3: Initial confirmation")
    confirm1 = input("Do you really want to delete ALL your ideas? (type 'DELETE' to continue): ")
    if confirm1 != 'DELETE':
        print("❌ Clear operation cancelled at step 1.")
        return
    
    # Second confirmation with count verification
    print(f"\n🔒 STEP 2/3: Verify the count")
    print(f"You are about to delete {total_count} ideas. Please confirm this number.")
    confirm2 = input(f"Type the exact number '{total_count}' to continue: ")
    if confirm2 != str(total_count):
        print("❌ Clear operation cancelled at step 2 - number mismatch.")
        return
    
    # Final confirmation with random safety phrase
    import random
    safety_phrases = ["CLEAR ALL IDEAS", "DELETE EVERYTHING", "REMOVE ALL DATA"]
    selected_phrase = random.choice(safety_phrases)
    
    print(f"\n🔒 STEP 3/3: Final safety confirmation")
    print(f"This is your last chance to cancel!")
    confirm3 = input(f"Type exactly '{selected_phrase}' to proceed with deletion: ")
    if confirm3 != selected_phrase:
        print("❌ Clear operation cancelled at step 3 - safety phrase mismatch.")
        return
    
    # Perform the deletion
    print("\n🗑️  Performing deletion...")
    deleted_files = []
    
    # Delete all month files
    for file in IDEA_DIR.glob('*.txt'):
        deleted_files.append(file.name)
        file.unlink()
    
    # Recreate basic structure
    setup_directory()
    
    print("✅ Deletion completed successfully!")
    print(f"📁 Deleted files: {', '.join(deleted_files)}")
    print("💡 You can now start fresh with new ideas!")
    print("🆕 Use 'idea \"your first new idea\"' to begin recording again.")

def count_ideas():
    """Count ideas statistics"""
    if not IDEA_DIR.exists():
        print("📝 No idea directory yet.")
        return

    total_count = 0
    month_files = list(IDEA_DIR.glob('????-??.txt'))
    
    if not month_files:
        print("💡 You haven't recorded any ideas yet")
        return
    
    print("📊 Idea Statistics:")
    print("=" * 30)
    
    for month_file in sorted(month_files, reverse=True):
        month = month_file.stem
        
        with open(month_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        idea_count = sum(1 for line in lines if line.strip().startswith('['))
        if idea_count > 0:
            print(f"📝 {month}: {idea_count} ideas")
            total_count += idea_count
    
    print("=" * 30)
    print(f"💡 Total: {total_count} ideas")

def run():
    """Program entry point, handle command line arguments."""
    # Setup on first run
    setup()

    # Create command line argument parser
    parser = argparse.ArgumentParser(
        description="💡 A simple CLI tool for quickly capturing ideas - ideajar",
        epilog="Example usage:\n"
               "  idea \"Build a tool for recording ideas\"  # Record an idea\n"
               "  idea                                    # View current month ideas\n"
               "  idea --all                              # View all ideas\n"
               "  idea --month 2024-09                    # View specific month\n"
               "  idea --months                           # List all months\n"
               "  idea --search keyword                   # Search ideas\n"
               "  idea --count                            # Count ideas\n"
               "  idea --clear                            # Clear all ideas (with safety confirmations)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Add positional argument
    parser.add_argument(
        'idea_text', 
        type=str, 
        nargs='*',  # Accept zero or more arguments
        default=None,
        help="The idea text you want to record (multiple words allowed without quotes)"
    )
    
    # Add optional arguments
    parser.add_argument(
        '--all', 
        action='store_true',
        help="Show all historical ideas"
    )
    
    parser.add_argument(
        '--month', 
        type=str,
        help="Show ideas for specific month (format: YYYY-MM)"
    )
    
    parser.add_argument(
        '--months', 
        action='store_true',
        help="List all months with records"
    )
    
    parser.add_argument(
        '--search', 
        type=str,
        help="Search for ideas containing specified keyword"
    )
    
    parser.add_argument(
        '--clear', 
        action='store_true',
        help="Clear all ideas (with multiple safety confirmations)"
    )
    
    parser.add_argument(
        '--count', 
        action='store_true',
        help="Count idea statistics"
    )

    args = parser.parse_args()

    if args.clear:
        clear_ideas()
    elif args.count:
        count_ideas()
    elif args.months:
        list_months()
    elif args.search:
        search_ideas(args.search)
    elif args.month:
        list_ideas(month=args.month)
    elif args.all:
        list_ideas(show_all=True)
    elif args.idea_text:  # This will be an empty list if no arguments provided
        # Join multiple words into a single string
        idea_text = ' '.join(args.idea_text)
        if idea_text.strip():  # Only add if there's actual content
            add_idea(idea_text)
        else:
            list_ideas()  # If empty, show list instead
    else:
        list_ideas()

# When this file is run as main program, call run()
if __name__ == '__main__':
    run()
