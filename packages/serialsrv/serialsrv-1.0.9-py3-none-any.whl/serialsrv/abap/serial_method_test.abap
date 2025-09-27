*&---------------------------------------------------------------------*
*& Report SERIAL_METHOD_TEST
*&---------------------------------------------------------------------*
*& This program demonstrates how to use the SERIAL_SERVICE_METHOD class
*& to call the serialsrv software and retrieve serial port data.
*& 
*& The class provides three main methods:
*& 1. call_serial_service - Get full response with all details
*& 2. get_serial_value - Get only the serial value
*& 3. test_connection - Test if server is reachable
*&
*& Author: Altay Kireççi (c)(p)2025-09
*&---------------------------------------------------------------------*

REPORT serial_method_test.

* Selection screen parameters
SELECTION-SCREEN BEGIN OF BLOCK b1 WITH FRAME TITLE TEXT-001.
PARAMETERS: p_host TYPE string DEFAULT 'localhost' OBLIGATORY,
            p_port TYPE string DEFAULT '7373' OBLIGATORY,
            p_time TYPE i DEFAULT 10 OBLIGATORY.
SELECTION-SCREEN END OF BLOCK b1.

SELECTION-SCREEN BEGIN OF BLOCK b2 WITH FRAME TITLE TEXT-002.
PARAMETERS: p_full AS CHECKBOX DEFAULT 'X',
            p_value AS CHECKBOX,
            p_test AS CHECKBOX.
SELECTION-SCREEN END OF BLOCK b2.

* Text elements
SELECTION-SCREEN BEGIN OF BLOCK b3 WITH FRAME TITLE TEXT-003.
SELECTION-SCREEN COMMENT /1(70) TEXT-004.
SELECTION-SCREEN COMMENT /1(70) TEXT-005.
SELECTION-SCREEN COMMENT /1(70) TEXT-006.
SELECTION-SCREEN END OF BLOCK b3.

* Data declarations
DATA: ls_result TYPE serial_service_method=>ty_serial_result,
      lv_value  TYPE string,
      lv_success TYPE abap_bool.

* Text symbols
SELECTION-SCREEN BEGIN OF BLOCK b4 WITH FRAME.
SELECTION-SCREEN COMMENT /1(70) TEXT-007.
SELECTION-SCREEN END OF BLOCK b4.

* Main program
START-OF-SELECTION.
  PERFORM main.

*&---------------------------------------------------------------------*
*& Form MAIN
*&---------------------------------------------------------------------*
FORM main.
  WRITE: / 'SerialSrv Method Test Program',
         / '==============================',
         /.

  " Test connection first
  IF p_test = 'X'.
    PERFORM test_connection.
  ENDIF.

  " Get full result
  IF p_full = 'X'.
    PERFORM get_full_result.
  ENDIF.

  " Get only value
  IF p_value = 'X'.
    PERFORM get_serial_value.
  ENDIF.

  WRITE: / 'Test completed successfully!'.
ENDFORM.

*&---------------------------------------------------------------------*
*& Form TEST_CONNECTION
*&---------------------------------------------------------------------*
FORM test_connection.
  WRITE: / 'Testing connection...'.

  TRY.
      lv_success = serial_service_method=>test_connection(
        iv_host = p_host
        iv_port = p_port
        iv_timeout = p_time
      ).
      
      IF lv_success = abap_true.
        WRITE: / '✅ Connection successful!'.
      ELSE.
        WRITE: / '❌ Connection failed!'.
      ENDIF.
      
    CATCH serial_service_method=>connection_error.
      WRITE: / '❌ Connection error occurred!'.
    CATCH serial_service_method=>timeout_error.
      WRITE: / '❌ Timeout error occurred!'.
  ENDTRY.
  
  WRITE: /.
ENDFORM.

*&---------------------------------------------------------------------*
*& Form GET_FULL_RESULT
*&---------------------------------------------------------------------*
FORM get_full_result.
  WRITE: / 'Getting full result...'.

  TRY.
      ls_result = serial_service_method=>call_serial_service(
        iv_host = p_host
        iv_port = p_port
        iv_timeout = p_time
      ).
      
      IF ls_result-success = abap_true.
        WRITE: / '✅ Data retrieved successfully!',
               / 'Value:', ls_result-value,
               / 'Message:', ls_result-message,
               / 'Mode:', ls_result-mode,
               / 'Result:', ls_result-result,
               / 'Timestamp:', ls_result-timestamp.
      ELSE.
        WRITE: / '❌ Error occurred:',
               / ls_result-error_text.
      ENDIF.
      
    CATCH serial_service_method=>connection_error.
      WRITE: / '❌ Connection error occurred!'.
    CATCH serial_service_method=>timeout_error.
      WRITE: / '❌ Timeout error occurred!'.
    CATCH serial_service_method=>parse_error.
      WRITE: / '❌ Parse error occurred!'.
  ENDTRY.
  
  WRITE: /.
ENDFORM.

*&---------------------------------------------------------------------*
*& Form GET_SERIAL_VALUE
*&---------------------------------------------------------------------*
FORM get_serial_value.
  WRITE: / 'Getting serial value...'.

  TRY.
      lv_value = serial_service_method=>get_serial_value(
        iv_host = p_host
        iv_port = p_port
        iv_timeout = p_time
      ).
      
      WRITE: / '✅ Serial Value:', lv_value.
      
    CATCH serial_service_method=>connection_error.
      WRITE: / '❌ Connection error occurred!'.
    CATCH serial_service_method=>timeout_error.
      WRITE: / '❌ Timeout error occurred!'.
    CATCH serial_service_method=>parse_error.
      WRITE: / '❌ Parse error occurred!'.
  ENDTRY.
  
  WRITE: /.
ENDFORM.
