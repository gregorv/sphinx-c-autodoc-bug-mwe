/**
 * Lorem Ipsum
*/


/**
 * A plain old typedef
 */
typedef int a_typedef_type;

/**
 * Opaque pointer to storage object
 */
typedef struct mwe_storage mwe_storage_t;

/** Callback function pointer
 *
*/
typedef bool (*mwe_callback_t)(mwe_storage_t *, int);

/** Configuration struct
*/
typedef struct mwe_config {
  /** good documentation */
  int stuff;

  /** Decode test callback */
  mwe_callback_t callback; 
} mwe_config_t;

/** Create a new storage object
 *
 * Args:
 *     config: Configuration for the new storage
 *
 * Return:
 *     Pointer to the new storage object, or NULL if an error occured.
*/
mwe_storage_t *mwe_function(const mwe_config_t *config);
