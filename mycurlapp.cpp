#include <stdio.h>
#include <curl/curl.h>
#include <cstdlib>
#include <cstring>

struct memory {
    char *response;
    size_t size;
};

static size_t write_callback(void *data, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    struct memory *mem = (struct memory *)userp;

    char *ptr = (char*) realloc(mem->response, mem->size + realsize +1);
    if(ptr == NULL)
        return 0; // out of memory!

    mem->response = ptr;
    memcpy(&(mem->response[mem->size]), data, realsize);
    mem->size += realsize;
    mem->response[mem->size] = 0;

    return realsize;
}

int main(void) {
    // Initialize the libcurl library
    CURL *curl = curl_easy_init();
    CURLcode res;

    char error[CURL_ERROR_SIZE];

    curl_global_init(CURL_GLOBAL_ALL);

    struct memory chunk = {0};

    if(curl) {
        // Set the URL to work on
        curl_easy_setopt(curl, CURLOPT_URL, "https://www.example.com/");
        // Set display verbose information
        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
        // Set error message buffer
        curl_easy_setopt(curl, CURLOPT_ERRORBUFFER, error);
        // Set include the header in the body output
        curl_easy_setopt(curl, CURLOPT_HEADER, 1L);
        // Send all data to this function
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        // Pass 'chunk' struct to the callback function
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &chunk);

        // Perform the request, res will get the return code
        res = curl_easy_perform(curl);

        // Check for errors
        if(res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n", error);

        // Always cleanup
        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();

    return 0;
}