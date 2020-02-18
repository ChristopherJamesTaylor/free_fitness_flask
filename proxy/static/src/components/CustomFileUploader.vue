<template>
    <div class="uploadBox">
        <form role="form" enctype="multipart/form-data" @submit.prevent="onSubmit">
            <!-- FILE UPLOADER BOX -->
            <div class="uploadBoxMain">
                <div class="form-group">
                    <div class="dropArea" @ondragover="onChange" :class="dragging ? 'dropAreaDragging' : ''" @dragenter="dragging=true" @dragend="dragging=false" @dragleave="dragging=false">
                        <h3>{{dropAreaPrimaryMessage}}</h3>
                        <input type="file" id="files" required multiple @change="onChange">
                    </div>
                </div>
            </div>

            <!-- FILE SUMMARY BOX -->
            <div class="uploadBoxMain" v-if="itemsAdded">

              <v-card>
                <v-toolbar class="headline grey lighten-2">
                  <v-toolbar-title>Files</v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" class="ma-2" @click="removeItems">{{removeFileMessage}}</v-btn>
                </v-toolbar>
                <v-list two-line>
                  <template v-for="(item, index) in currFiles">
                    <v-list-item
                      ripple
                      @click=""
                      :key="item.name"
                    >
                      <v-list-item-content>
                        <v-list-item-title>{{ item.name }}</v-list-item-title>
                        <v-list-item-subtitle class="text--primary">{{ item.type }}</v-list-item-subtitle>
                      </v-list-item-content>

                      <v-list-item-action>
                        <v-list-item-action-text>{{ item.size }} KB</v-list-item-action-text>
                      </v-list-item-action>

                    </v-list-item>
                    <v-divider v-if="index + 1 < itemsNames.length" :key="index"></v-divider>
                  </template>
                  <v-list-item
                    ripple
                    key="itemsTotalSize"
                  >
                    <v-list-item-content>
                      <v-list-item-title>{{  }}</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-list-item-action-text>{{ itemsTotalSize }} KB</v-list-item-action-text>
                    </v-list-item-action>
                  </v-list-item>
                </v-list>
              </v-card>
                <!-- <p><strong>{{fileNameMessage}}</strong></p>
                <ol>
                    <li v-for="name in itemsNames">{{name}}</li>
                </ol>
                <p><strong>{{fileSizeMessage}}</strong></p>
                <ol>
                    <li v-for="size in itemsSizes">{{size}}</li>
                </ol>
                <p><strong>{{totalFileMessage}}</strong> {{itemsAdded}}</p>
                <p><strong>{{totalUploadSizeMessage}}</strong> {{itemsTotalSize}}</p>
                <v-btn color="primary" @click="removeItems">{{removeFileMessage}}</v-btn>

                <div class="loader" v-if="isLoaderVisible">
                    <div class="loaderImg"></div>
                </div> -->
            </div>

            <!-- <div>
                <v-btn color="primary" type="button" @click="removeItems">{{cancelButtonMessage}}</v-btn>
            </div> -->
            <br>
            <div class="successMsg" v-if="successMsg !== ''">{{successMsg}}</div>
            <div class="errorMsg" v-if="errorMsg !== ''">{{fileUploadErrorMessage}}:<br>{{errorMsg}} <br>{{retryErrorMessage}}</div>
            <div class="errorMsg" v-if="itemsAdded && itemsAdded < minItems">{{minFilesErrorMessage}}: {{minItems}}.  <br>{{retryErrorMessage}} </div>
            <div class="errorMsg" v-if="itemsAdded && itemsAdded > maxItems">{{maxFilesErrorMessage}}: {{maxItems}}.  <br>{{retryErrorMessage}}</div>
        </form>
    </div>
</template>

<script>
// require('es6-promise').polyfill();
component: {axios}
export default {
    props: {
        postURL: {
            type: String,
            required: true
        },
        minItems: {
            type: Number,
            default: 1
        },
        maxItems: {
            type: Number,
            default: 30
        },
        method: {
            type: String,
            default: 'post'
        },
        postData: {
            type: [Object],
            default: () => {}
        },
        postHeader:{
          type: [Object],
          default: () => {}
        },
        successMessagePath: {
            type: String,
            required: true
        },
        errorMessagePath: {
            type: String,
            required: true
        },
        dropAreaPrimaryMessage: {
          type: String,
          default: 'Add Files'
        },
        fileNameMessage: {
          type: String,
          default: 'Names'
        },
        fileSizeMessage: {
          type: String,
          default: 'Sizes'
        },
        totalFileMessage: {
          type: String,
          default: 'Total files:'
        },
        totalUploadSizeMessage: {
          type: String,
          default: 'Total upload size:'
        },
        removeFileMessage: {
          type: String,
          default: 'Remove files'
        },
        uploadButtonMessage: {
          type: String,
          default: 'Upload'
        },
        cancelButtonMessage: {
          type: String,
          default: 'Cancel'
        },
        fileUploadErrorMessage: {
          type: String,
          default: 'An error has occurred'
        },
        minFilesErrorMessage: {
          type: String,
          default: 'Minimum files that need to be added to uploader'
        },
        maxFilesErrorMessage:  {
          type: String,
          default: 'Maximum files that can be added to uploader'
        },
        retryErrorMessage: {
          type: String,
          default: 'Please remove the files and try again.'
        },
        httpMethodErrorMessage: {
          type: String,
          default: "This HTTP method is not allowed. Please use either 'put' or 'post' methods."
        },
        showHttpMessages: {
          type: Boolean,
          default: true
        }
    },

    /*
     * The component's data.
     */
    data() {
        return {
            dragging: false,
            items: [],
            itemsAdded: '',
            itemsNames: [],
            itemsSizes: [],
            itemsTotalSize: '',
            formData: new FormData(),
            currFiles: [],
            successMsg: '',
            errorMsg: '',
            isLoaderVisible: false,
            fileSizes: 0
        }
    },

    methods: {
        // http://scratch99.com/web-development/javascript/convert-bytes-to-mb-kb/
        bytesToSize(bytes) {
            const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
            if (bytes === 0) return 'n/a';
            let i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
            if (i === 0) return bytes + ' ' + sizes[i];
            return (bytes / Math.pow(1024, i)).toFixed(2) + ' ' + sizes[i];
        },

        onChange(e) {
            this.successMsg = '';
            this.errorMsg = '';
            // this.formData = new FormData();
            let files = e.target.files || e.dataTransfer.files;
            this.itemsAdded = files.length;
            // let fileSizes = 0;
            for (let x in files) {
                if (!isNaN(x)) {
                    this.items = e.target.files[x] || e.dataTransfer.files[x];
                    this.itemsNames.push(files[x].name);
                    this.itemsSizes.push(this.bytesToSize(files[x].size));
                    this.fileSizes += files[x].size;
                    // taylor orignal 18th Nov 2019
                    //this.formData.append('files[]', this.items);
                    var currFile = {
                      'name': files[x].name,
                      'size': this.bytesToSize(files[x].size),
                      'type': files[x].type
               }
                    this.currFiles.push(currFile);
                    this.formData.append('files[]', this.items, files[x].name);
                }
            }
            console.log('Trigger Emit for File Data');
            console.log(this.formData)
            console.log(this.formData)
            this.$emit('event_notify',this.formData);
            this.itemsTotalSize = this.bytesToSize(this.fileSizes);
        },

        removeItems() {
            this.items = '';
            this.itemsAdded = '';
            this.itemsNames = [];
            this.itemsSizes = [];
            this.itemsTotalSize = '';
            this.dragging = false;
            this.currFiles = [];
            this.formData = new FormData()
        },

        callback(data) {
          console.log('I am callback in custom')
          this.$emit('event_callback',data)
        },

        onSubmit() {
            this.isLoaderVisible = true;

            if(typeof this.postData ==='object' && this.postData !== null && Object.keys(this.postData).length > 0){
              for(var key in this.postData){
                this.formData.append(key, this.postData[key]);
              }
            }
        },
    }
}
</script>

<style>
.uploadBox {
    position: relative;
    padding: 0 1em 1em 1em;
    margin: 1em;
}

.uploadBox h3 {
    padding-top: 1em;
}

.uploadBox .uploadBoxMain {
    position: relative;
    margin-bottom: 1em;
    margin-right: 1em;
}

/* Drag and drop */
.uploadBox .dropArea {
    position: relative;
    width: 100%;
    height: 300px;
    border: 5px dashed #3D85C6;
    text-align: center;
    font-size: 2em;
    padding-top: 80px;
}

.uploadBox .dropArea input {
    position: absolute;
    cursor: pointer;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
}
/* End drag and drop */

/* Loader */
.uploadBox .loader {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    opacity: 0.9;
}

.uploadBox .loaderImg {
    border: 9px solid #eee;
    border-top: 9px solid #00ADCE;
    border-radius: 50%;
    width: 70px;
    height: 70px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
/* End Loader */

.uploadBox .errorMsg {
    font-size: 2em;
    color: #a94442;
}

.uploadBox .successMsg {
    font-size: 2em;
    color: #3c763d;
}
</style>