#!/bin/bash
# Master Samsung Debloat Script
# Orchestrates individual phase scripts for clean execution
# Each phase can be run independently or skipped as needed

set -e  # Exit on error

DEVICE="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

usage() {
    cat <<EOF
Usage: $0 <device-ip:port> [options]

Arguments:
  device-ip:port    ADB device identifier (e.g., 192.168.87.245:44577)

Options:
  --skip-phase N    Skip phase N (can be specified multiple times)
  --only-phase N    Run only phase N
  --dry-run         Show what would be executed without running
  --help            Show this help message

Phases:
  1. Initial debloat (37 packages: Bixby, Samsung Daily, AR Zone, etc.)
  2. Additional bloat (28 packages: Verizon, Microsoft, Samsung services)
  3. Aggressive Samsung (24 packages: Smart features, Game services, Pay)
  4. Disable duplicates (7 apps: Dialer, Contacts, Gallery, etc.)
  5. UI overlays (5 packages: Theme, personalization, lock screen)
  6. Behavior overrides (18 packages: Settings helpers, usage tracking)
  7. Grant permissions (31 permissions for 10 Google apps)

Examples:
  $0 192.168.87.245:44577
  $0 192.168.87.245:44577 --skip-phase 4
  $0 192.168.87.245:44577 --only-phase 1 --dry-run

EOF
    exit 1
}

log() {
    echo -e "${GREEN}[$(date +'%H:%M:%S')]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

run_phase() {
    local phase_num=$1
    local phase_name=$2
    local script_name=$3
    local description=$4

    # Check if phase should be skipped
    for skip in "${SKIP_PHASES[@]}"; do
        if [ "$skip" == "$phase_num" ]; then
            warn "Skipping Phase $phase_num: $phase_name"
            return 0
        fi
    done

    # Check if running only specific phase
    if [ ${#ONLY_PHASES[@]} -gt 0 ]; then
        local run_this=false
        for only in "${ONLY_PHASES[@]}"; do
            [ "$only" == "$phase_num" ] && run_this=true
        done
        [ "$run_this" == false ] && return 0
    fi

    echo ""
    log "===== Phase $phase_num: $phase_name ====="
    log "$description"

    local script_path="$SCRIPT_DIR/executed/$script_name"

    if [ ! -f "$script_path" ]; then
        error "Script not found: $script_path"
    fi

    if [ "$DRY_RUN" == true ]; then
        warn "DRY RUN: Would execute $script_name"
        return 0
    fi

    adb -s "$DEVICE" shell < "$script_path"
    local exit_code=$?

    if [ $exit_code -eq 0 ]; then
        log "Phase $phase_num completed successfully"
    else
        warn "Phase $phase_num completed with some failures (exit code: $exit_code)"
    fi
}

# Parse arguments
SKIP_PHASES=()
ONLY_PHASES=()
DRY_RUN=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-phase)
            SKIP_PHASES+=("$2")
            shift 2
            ;;
        --only-phase)
            ONLY_PHASES+=("$2")
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help)
            usage
            ;;
        *)
            if [ -z "$DEVICE" ]; then
                DEVICE="$1"
                shift
            else
                error "Unknown argument: $1"
            fi
            ;;
    esac
done

# Validate device argument
if [ -z "$DEVICE" ]; then
    error "Device IP:port required"
    usage
fi

# Verify ADB connection
log "Verifying connection to $DEVICE..."
if ! adb -s "$DEVICE" get-state >/dev/null 2>&1; then
    error "Cannot connect to device $DEVICE. Is wireless ADB enabled?"
fi

log "Connected to $DEVICE"
log "Starting debloat process..."

# Run phases
run_phase 1 "Initial Debloat" "debloat.adb.sh" \
    "Removing Bixby, Samsung Daily, AR Zone, Samsung apps..."

run_phase 2 "Additional Bloat" "additional-bloat.adb.sh" \
    "Removing Verizon, Microsoft, Samsung themes and services..."

run_phase 3 "Aggressive Samsung Debloat" "aggressive-samsung-debloat.adb.sh" \
    "Removing Smart features, Game services, behavior overrides..."

run_phase 4 "Disable Samsung Duplicates" "disable-samsung-duplicates.adb.sh" \
    "Disabling deeply-integrated Samsung apps (Dialer, Contacts, Gallery)..."

run_phase 5 "UI Overlays" "remove-samsung-ui-overlays.adb.sh" \
    "Removing UI customizations and theme components..."

run_phase 6 "Behavior Overrides" "remove-behavior-overrides.adb.sh" \
    "Removing settings helpers, usage tracking, behavior modifications..."

run_phase 7 "Grant Permissions" "grant-app-permissions.adb.sh" \
    "Granting essential permissions to Google apps..."

# Summary
echo ""
log "===== Debloat Complete! ====="
echo ""
echo "Packages removed: ~87"
echo "Packages disabled: ~8"
echo ""
echo "Next steps:"
echo "1. Install Google apps from Play Store (see README.md)"
echo "2. Set defaults: Gboard, Lawnchair, Google Phone, Google Messages"
echo "3. Star family contacts in Google Contacts"
echo "4. Configure Do Not Disturb priority notifications"
echo ""
log "See README.md for complete setup instructions"
