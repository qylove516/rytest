"""
最外层:
	//index 函数 里面加入的//
	'app_list':
	'title': '站点管理',
	//each_context 函数里面加入的//
	'available_apps':
	'has_permission': True,
	'site_url': '/',
	'site_header': 'Django 管理',
	'site_title': 'Django 站点管理员'
"""

index = {
	'available_apps': [{
		'has_module_perms': True,
		'app_url': '/admin/goods/',
		'name': '商品',
		'models': [{
			'add_url': '/admin/goods/price/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Price',
			'view_only': False,
			'name': '价格',
			'admin_url': '/admin/goods/price/'
		}, {
			'add_url': '/admin/goods/goods/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Goods',
			'view_only': False,
			'name': '商品',
			'admin_url': '/admin/goods/goods/'
		}, {
			'add_url': '/admin/goods/shop/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Shop',
			'view_only': False,
			'name': '商家',
			'admin_url': '/admin/goods/shop/'
		}],
		'app_label': 'goods'
	}, {
		'has_module_perms': True,
		'app_url': '/admin/auth/',
		'name': '认证和授权',
		'models': [{
			'add_url': '/admin/auth/user/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'User',
			'view_only': False,
			'name': '用户',
			'admin_url': '/admin/auth/user/'
		}, {
			'add_url': '/admin/auth/group/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Group',
			'view_only': False,
			'name': '组',
			'admin_url': '/admin/auth/group/'
		}],
		'app_label': 'auth'
	}],
	'app_list': [{
		'has_module_perms': True,
		'app_url': '/admin/goods/',
		'name': '商品',
		'models': [{
			'add_url': '/admin/goods/price/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Price',
			'view_only': False,
			'name': '价格',
			'admin_url': '/admin/goods/price/'
		}, {
			'add_url': '/admin/goods/goods/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Goods',
			'view_only': False,
			'name': '商品',
			'admin_url': '/admin/goods/goods/'
		}, {
			'add_url': '/admin/goods/shop/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Shop',
			'view_only': False,
			'name': '商家',
			'admin_url': '/admin/goods/shop/'
		}],
		'app_label': 'goods'
	}, {
		'has_module_perms': True,
		'app_url': '/admin/auth/',
		'name': '认证和授权',
		'models': [{
			'add_url': '/admin/auth/user/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'User',
			'view_only': False,
			'name': '用户',
			'admin_url': '/admin/auth/user/'
		}, {
			'add_url': '/admin/auth/group/add/',
			'perms': {
				'delete': True,
				'change': True,
				'add': True,
				'view': True
			},
			'object_name': 'Group',
			'view_only': False,
			'name': '组',
			'admin_url': '/admin/auth/group/'
		}],
		'app_label': 'auth'
	}],
	'has_permission': True,
	'title': '站点管理',
	'site_url': '/',
	'site_header': 'Django 管理',
	'site_title': 'Django 站点管理员'
}

