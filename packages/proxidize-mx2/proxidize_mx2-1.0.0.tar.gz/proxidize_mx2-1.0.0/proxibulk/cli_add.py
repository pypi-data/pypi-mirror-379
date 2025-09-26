def bulk_set_default_apn(modems: List[Modem]):
    """Select an APN profile and set it as default for all modems in a group."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems in this group to update.", COLOR_RED)
        return
    
    # For a batch operation, we'll get the APN profiles from the first modem
    # and apply the selected profile ID to all modems
    first_modem = reachable_modems[0]
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" BULK SET DEFAULT APN PROFILE ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BOLD)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_BLUE)
    
    try:
        # Fetch available profiles from the first modem
        print_colored("\nFetching available APN profiles from the first modem...", COLOR_YELLOW)
        ok, profiles = get_apn_profiles(first_modem)
        
        if not ok or not profiles:
            print_colored("No APN profiles found or error retrieving profiles.", COLOR_RED)
            return
        
        # Display available profiles
        print_colored("\nAvailable APN Profiles:", COLOR_BOLD)
        for i, profile in enumerate(profiles, 1):
            is_default = profile.get("Default", 0) == 1
            profile_id = profile.get("ProfileID", "Unknown")
            profile_name = profile.get("ProfileName", "Unknown")
            apn = profile.get("APN", "")
            
            status = "[DEFAULT]" if is_default else ""
            status_color = COLOR_GREEN if is_default else ""
            
            print_colored(f"  {i}. Profile {profile_id}: {profile_name} {status}", 
                         COLOR_BLUE + status_color)
            print_colored(f"     APN: {apn}", COLOR_BLUE)
        
        # Ask which profile to set as default
        choice = input("\nEnter number of profile to set as default for ALL modems (or 'q' to cancel): ").strip()
        
        if choice.lower() == 'q':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        try:
            choice_num = int(choice)
            if choice_num < 1 or choice_num > len(profiles):
                print_colored("Invalid profile number.", COLOR_RED)
                return
            
            selected_profile = profiles[choice_num - 1]
            profile_id = selected_profile.get("ProfileID")
            profile_name = selected_profile.get("ProfileName", "Unknown")
            
            # Confirm selection
            confirm = input(f"\nSet profile '{profile_name}' (ID: {profile_id}) as default for ALL modems? (y/n): ").strip().lower()
            if confirm != 'y':
                print_colored("Operation cancelled.", COLOR_YELLOW)
                return
            
            # Execute in bulk
            _bulk_execute(
                reachable_modems,
                lambda m: set_default_apn_profile(m, profile_id),
                "set default APN profile"
            )
                
        except ValueError:
            print_colored("Invalid input. Please enter a valid number.", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)
