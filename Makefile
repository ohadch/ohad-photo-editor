NAMESPACE=photo-editor

up:
	docker-compose up -docker
down:
	docker-compose down
up-k8s:
	# Update helm dependencies
	@echo "Updating helm dependencies"
	helm dependency update helm/ohad-photo-editor

	# Install the chart
	@echo "Installing the chart"
	helm upgrade --install \
		ohad-photo-editor \
		helm/ohad-photo-editor \
		--create-namespace \
		-n $(NAMESPACE)
down-k8s:
	helm uninstall ohad-photo-editor -n $(NAMESPACE)
local-registry-up:
	docker-compose -f docker-compose-registry.yml up -d
local-registry-down:
	docker-compose -f docker-compose-registry.yml down
