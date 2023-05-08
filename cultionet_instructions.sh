# Cultionet Instructions:

cd /home/ubuntu/Geography
ln -s Geography/time_series_vars time_series_vars
ln -s Geography/user_train user_train


# Create Training files
cultionet create \
        --project-path . \
        --config-file config.yml \
        --crop-column class \
        --grid-size 100 100 \
        --max-crop-class 1 \
        --image-date-format %Y%j \
        --feature-pattern {region}/{image_vi} \
        --start-date 04-01 \
        --end-date 04-01 \
        --transforms none fliplr flipud rot90 rot180 rot270 tswarp tsnoise gaussian saltpepper speckle


# Train the model
cultionet train \
        --project-path . \
        --expected-dim 4 \
        --expected-height 100 \
        --expected-width 100 \
        --delete-mismatches \
        --recalc-zscores \
        --val-frac 0.2 \
        --random-seed 500 \
        --batch-size 4 \
        --epochs 2 \
        --filters 16 \
        --device gpu \
        --patience 5 \
        --learning-rate 0.001 \
        --optimizer SGD \
        --reset-model


# Fine-Tuning Train - (Optional)
#v1: learning rate: 0.0001, optimizer: AdamW, Epoch 10, filters 32, --activation-type SiLU (default)
# v2: learning rate: 0.0001, optimizer: SGD, Epoch 10, --activation-type SiLU (default)
# v3: learning rate: 0.001, optimizer: AdamW, Epoch 10, --activation-type SiLU (default)
#v4: learning rate: 0.0001, optimizer: AdamW, Epoch: 15, --activation-type SiLU (default)
# v4: learning rate: 0.0001, optimizer: AdamW, Epoch: 15, --activation-type ReLU
cultionet train \
  --project-path . \
	--expected-dim 4 \
	--expected-height 100 \
	--expected-width 100 \
	--delete-mismatches \
	--recalc-zscores \
	--val-frac 0.2 \
	--random-seed 500 \
	--activation-type ReLU \
	--batch-size 4 \
	--epochs 10 \
	--filters 32 \
	--device gpu \
	--patience 5 \
	--learning-rate 0.0001 \
	--reset-model


# Testing UNet3Psi ########

# v4: learning rate: 0.0001, optimizer: AdamW, Epoch: 15, --model-type UNet3Psi
cultionet train \
  --project-path . \
	--expected-dim 4 \
	--expected-height 100 \
	--expected-width 100 \
	--delete-mismatches \
	--recalc-zscores \
	--val-frac 0.2 \
	--random-seed 500 \
	--batch-size 5 \
	--epochs 10 \
	--filters 32 \
	--device gpu \
	--patience 5 \
	--model-type UNet3Psi \
	--dilations 2 \
	--learning-rate 0.0001 \
	--reset-model
# Run the code from 06_rechunk_image for all the images in a region file.

# Create - predict with original images:

cultionet create-predict \
	--project-path . \
	-y 2022 \
	--ts-path inference/000007/ \
	--res 0.00008983152841195214829 \
	--image-date-format %Y%j \
	--append-ts n \
	--num-workers 4  \
	--feature-pattern inference/{region}/{image_vi} \
	--start-date 04-01 \
	--end-date 04-01 \
	--config-file config.yml


# create - prediction files on rechunked Images

cultionet create-predict \
	--project-path . \
	-y 2022 \
	--ts-path inference_rechunk/000007/ \
	--res 0.00008983152841195214829 \
	--image-date-format %Y%j \
	--append-ts n \
	--num-workers 4  \
	--feature-pattern inference/{region}/{image_vi} \
	--start-date 04-01 \
	--end-date 04-01 \
	--config-file config.yml



# ======Predict on RECHUNKED IMAGES========

cultionet predict \
  	  -p . -y 2022 -o predictions/predictions_000007_relu.tif \
  	  -d data/predict/processed/ --region 000007 \
  	  --ref-image inference_rechunk/000007/evi/2021182.tif \
  	  --batch-size 4 --config-file config.yml


# ========== Evaluation and other metrics

# Step 1:
# Run the below from the main AWS Terminal window
tensorboard --logdir ./ckpt/lightning_logs

# Step 2: Set up port forwarding through SSH
# Open another terminal window in the local machine
ssh -i path/to/your/private/key.pem -L 6006:localhost:6006 ec2-user@your-aws-instance-public-ip

# Example
ssh -i /Users/varunshah/Documents/GWU/Semester\ 4/Geography/AWS_Key/private_key.pem -L 6006:localhost:6006 ubuntu@54.224.25.162

# Step 3:
'''
Go the the local browser and open: http://localhost:6006
'''




