#!/usr/bin/env python3
"""
OPERATION AETHERFALL // SAFEHOUSE EMERGENCY DISARM TERMINAL
Facility: Thrissur Safehouse Node (KL-08)
Presented by: FOSS GECT x GECT Film Society
"""

import sys
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def main():
    clear()
    print("=" * 75)
    print("  OPERATION AETHERFALL // SAFEHOUSE EMERGENCY TERMINAL")
    print("  PRESENTED BY: FOSS GECT (FOSS CELL GECT) × GECT FILM SOCIETY")
    print("  LOCATION: THRISSUR GROUND NODE (KL-08)")
    print("  ACTIVE TIMER: 02:00:00 [COUNTING DOWN]")
    print("=" * 75)
    print("\n\"IF YOU FOUND THIS, YOU FOLLOWED THE TRAIL. DO NOT TRUST THE STORY YOU WERE GIVEN.\"\n")
    
    print("-" * 75)
    print("STEP 1: PHYSICAL COORDINATE VERIFICATION")
    print("-" * 75)
    lat = input("Enter Latitude (from lab_photo.png metadata, e.g. 10.5276): ").strip().replace("LAT_", "").replace("°N", "").strip()
    lon = input("Enter Longitude (from floor_blueprint.png whiteboard match, e.g. 76.2144): ").strip().replace("LON_", "").replace("°E", "").strip()

    if "10.5276" not in lat or "76.2144" not in lon:
        print("\n\033[91m[-] ERROR: Coordinates rejected! Position does not match safehouse calibration.\033[0m")
        print("[-] Check lab_photo.png metadata and floor_blueprint.png calibration axis.")
        return

    print("\n\033[92m[+] GEOLOCATION AUTHENTICATED: 10.5276° N, 76.2144° E (Thrissur Ground Zero)\033[0m")
    
    print("\n" + "-" * 75)
    print("STEP 2: ROOT MASTER AUTHORIZATION")
    print("-" * 75)
    key = input("Enter full master passcode (Format: AETHER_OCT2-9042-304): ").strip().upper()

    if key != "AETHER_OCT2-9042-304" and key != "AETHERFALL":
        print("\n\033[91m[-] INVALID MASTER KEY. Server wipe countdown continues!\033[0m")
        print("[-] Combine Key 1 (AETHER_) + Key 2 (OCT2-9042-304).")
        return

    # Trigger Climax
    clear()
    print("\n\033[92m" + "=" * 75)
    print("[!] CRITICAL SYSTEM OVERRIDE ACCEPTED — SENTINEL-AI PURGE ABORTED!")
    print("=" * 75 + "\033[0m")
    time.sleep(1.2)
    
    typewriter("\nTRANSMITTING DECRYPTION TELEMETRY TO EXTERNAL REPOSITORIES...", 0.02)
    time.sleep(0.6)
    typewriter("SYNCHRONIZING WITH FOSS GECT SECURITY ARCHIVES...", 0.02)
    time.sleep(0.6)
    typewriter("ISOLATING JOHN VANCE'S UNAUTHORIZED SURVEILLANCE MODULES...", 0.02)
    time.sleep(0.8)

    print("\n\033[96m" + "=" * 75)
    typewriter("AETHERFALL PROTOCOL: COMPLETE", 0.02)
    typewriter("EVIDENCE RECOVERED", 0.02)
    typewriter("SERVER WIPE: STOPPED", 0.02)
    typewriter("COPIES SAVED TO EXTERNAL SERVERS", 0.02)
    typewriter("CASE STATUS: EXPOSED", 0.02)
    print("=" * 75 + "\033[0m")
    time.sleep(1.0)

    print("\n\033[93m" + "-" * 75)
    typewriter("If you are seeing this, the evidence survived.", 0.025)
    typewriter("You were never meant to find me.", 0.025)
    typewriter("You were meant to find the truth.", 0.025)
    typewriter("— E. ROSTOVA", 0.03)
    print("-" * 75 + "\033[0m\n")
    time.sleep(2.0)

    print("\033[90m[The monitor goes black.]\033[0m")
    time.sleep(1.5)
    print("\033[90m[For a few seconds, nobody speaks. Then a final message appears:]\033[0m\n")
    time.sleep(1.5)

    print("\033[92m" + "*" * 75)
    print("                             CASE  CLOSED")
    print("*" * 75 + "\033[0m")
    time.sleep(1.0)
    typewriter("The evidence you recovered is automatically saved to an external server.", 0.02)
    typewriter("The countdown disappears.", 0.02)
    typewriter("Somewhere in the distance, a chime sound echoes through the abandoned facility.", 0.02)
    print()
    typewriter('"YOU DIDN\'T FIND ME. YOU FOUND WHAT I LEFT BEHIND."', 0.035)
    print()
    typewriter("The screen shuts down completely. Then, from the recovered files,", 0.02)
    typewriter("one last detail becomes clear: Dr. Elena Rostova is still alive.", 0.02)
    typewriter("The investigation is over. The truth is not.", 0.025)
    print("\n\033[92m======================= END OF OPERATION AETHERFALL =======================\033[0m")
    print("               CONGRATULATIONS FROM FOSS GECT × GECT FILM SOCIETY!          \n")

if __name__ == "__main__":
    main()
