#!/usr/bin/env bash
# 사용: scripts/new_post.sh <explainer|tutorial|paper-note|technical-note> <chapter> <section> <slug>
set -e
T=$1; CH=$(printf "%02d" $2); SEC=$(printf "%02d" $3); SLUG=$4
D="posts/ch${CH}-${SEC}-${SLUG}"
mkdir -p "$D"
sed -e "s/^book-chapter: .*/book-chapter: $2/" -e "s/^book-section: .*/book-section: $3/" \
    -e "s/^date: .*/date: $(date +%F)/" "posts/_templates/${T}.qmd" > "$D/index.qmd"
echo "created $D/index.qmd"
