#!/bin/bash
# Grant essential permissions to Google apps

echo "Granting permissions for Google Phone..."
pm grant com.google.android.dialer android.permission.READ_CONTACTS
pm grant com.google.android.dialer android.permission.WRITE_CONTACTS
pm grant com.google.android.dialer android.permission.READ_CALL_LOG
pm grant com.google.android.dialer android.permission.WRITE_CALL_LOG
pm grant com.google.android.dialer android.permission.CALL_PHONE
pm grant com.google.android.dialer android.permission.READ_PHONE_STATE
pm grant com.google.android.dialer android.permission.CAMERA

echo "Granting permissions for Google Contacts..."
pm grant com.google.android.contacts android.permission.READ_CONTACTS
pm grant com.google.android.contacts android.permission.WRITE_CONTACTS
pm grant com.google.android.contacts android.permission.GET_ACCOUNTS

echo "Granting permissions for Google Messages..."
pm grant com.google.android.apps.messaging android.permission.READ_SMS
pm grant com.google.android.apps.messaging android.permission.SEND_SMS
pm grant com.google.android.apps.messaging android.permission.RECEIVE_SMS
pm grant com.google.android.apps.messaging android.permission.READ_CONTACTS
pm grant com.google.android.apps.messaging android.permission.CAMERA

echo "Granting permissions for Google Photos..."
pm grant com.google.android.apps.photos android.permission.READ_MEDIA_IMAGES
pm grant com.google.android.apps.photos android.permission.READ_MEDIA_VIDEO
pm grant com.google.android.apps.photos android.permission.ACCESS_MEDIA_LOCATION
pm grant com.google.android.apps.photos android.permission.CAMERA

echo "Granting permissions for Files by Google..."
pm grant com.google.android.apps.nbu.files android.permission.READ_EXTERNAL_STORAGE
pm grant com.google.android.apps.nbu.files android.permission.WRITE_EXTERNAL_STORAGE

echo "Granting permissions for Google Calendar..."
pm grant com.google.android.calendar android.permission.READ_CALENDAR
pm grant com.google.android.calendar android.permission.WRITE_CALENDAR
pm grant com.google.android.calendar android.permission.READ_CONTACTS

echo "Granting permissions for Gmail..."
pm grant com.google.android.gm android.permission.GET_ACCOUNTS
pm grant com.google.android.gm android.permission.READ_CONTACTS

echo "Granting permissions for Chrome..."
pm grant com.android.chrome android.permission.ACCESS_FINE_LOCATION
pm grant com.android.chrome android.permission.CAMERA

echo "Granting permissions for Google Keep..."
pm grant com.google.android.keep android.permission.RECORD_AUDIO
pm grant com.google.android.keep android.permission.CAMERA

echo "Granting permissions for Google Clock..."
pm grant com.google.android.deskclock android.permission.RECORD_AUDIO

echo "Granting notification access for key apps..."
# Note: Notification permissions on Android 13+ need to be granted via settings or first launch

echo "Done! Some permissions may require manual approval on first app launch."
